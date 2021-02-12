from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from medicSearch.models.Profile import Profile
from medicSearch.forms.AuthForm import LoginForm, RegisterForm, RecoveryForm, ChangePasswordForm
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import hashlib

def login_view(request):
    loginForm = LoginForm()
    message = None

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        loginForm = LoginForm(request.POST)

        if loginForm.is_valid():
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                _next = request.GET.get('next')
                if _next is not None:
                    return redirect(_next)
                else:
                    return redirect("/")
            else:
                message = {
                    'type': 'danger',
                    'text': 'Dados de usuário incorretos'
                }

    context = {
        'form': loginForm,
        'message': message,
        'title': 'Login',
        'button_text': 'Entrar',
        'link_text': 'Registrar',
        'link_href': '/register'
    }

    
    return render(request, template_name='auth/auth.html', context=context, status=200)

def register_view(request):
    registerForm = RegisterForm()
    message = None

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        registerForm = RegisterForm(request.POST)

        if registerForm.is_valid():
            # Aqui verificamos se existe usuário ou e-mail com esse cadastro
            verifyUsername = User.objects.filter(username=username).first()
            verifyEmail = User.objects.filter(email=email).first()

            if verifyUsername is not None:
                message = { 'type': 'danger', 'text': 'Já existe um usuário com este username!' }
            elif verifyEmail is not None:
                message = { 'type': 'danger', 'text': 'Já existe um usuário com este e-mail!' }
            else:
                user = User.objects.create_user(username, email, password)
                if user is not None:
                    message = { 'type': 'success', 'text': 'Conta criada com sucesso!' }
                else:
                    message = { 'type': 'danger',  'text': 'Um erro ocorreu ao tentar criar o usuário.' }

    context = {
        'form': registerForm,
        'message': message,
        'title': 'Registrar',
        'button_text': 'Registrar',
        'link_text': 'Login',
        'link_href': '/login'
    }
    return render(request, template_name='auth/auth.html', context=context, status=200)

def logout_view(request):
    logout(request)
    return redirect('/login')

def recovery_view(request):
    recoveryForm = RecoveryForm()
    message = None

    if request.method == 'POST':
        recoveryForm = RecoveryForm(request.POST)

        if recoveryForm.is_valid():
            email = request.POST['email']
            profile = Profile.objects.filter(user__email=email).first()
            if profile is not None:
                try:
                    send_email(profile)
                    message = {
                        'type': 'success',
                        'text': 'Um e-mail foi enviado para sua caixa de entrada.'
                    }
                except:
                    message = { 'type': 'danger', 'text': 'Erro no envio do e-mail.' }
            else:
                message = { 'type': 'danger', 'text': 'E-mail inexistente.' }
        else:
            message = { 'type': 'danger', 'text': 'Formulário inválido' }

    context = {
        'form': recoveryForm,
        'message': message,
        'title': 'Recuperar senha',
        'button_text': 'Recuperar',
        'link_text': 'Login',
        'link_href': '/login'
    }
    return render(request, template_name='auth/auth.html', context=context, status=200)

def send_email(profile):
    profile.token = hashlib.sha256().hexdigest()
    profile.save()
    try:
        html_message = render_to_string('auth/recovery.html', {'token': profile.token})
        message = strip_tags(html_message)
        send_mail(
            subject="Recuperação de senha", message=message, html_message=html_message,
            from_email=settings.EMAIL_HOST_USER, recipient_list=[profile.user.email], fail_silently=False,
        )
    except:
        raise Exception    

def change_password(request, token):
    profile = Profile.objects.filter(token=token).first()
    changePasswordForm = ChangePasswordForm()
    message = None
    link_text = 'Solicitar recuperação de senha'
    link_href = '/recovery'

    if profile is not None:
        if request.method == 'POST':
            changePasswordForm = ChangePasswordForm(request.POST)
            if changePasswordForm.is_valid():
                profile.user.set_password(request.POST['password'])
                profile.token = None
                profile.user.save()
                profile.save()
                message = { 'type': 'success', 'text': 'Senha alterada com sucesso!!!' }
                link_text = 'Login'
                link_href = '/login'
            else:
                message = { 'type': 'danger', 'text': 'Formulário inválido.' }
    else:
        message = { 'type': 'danger', 'text': 'Token inválido. Solicite novamente' }

    context = {
        'form': changePasswordForm,
        'message': message,
        'title': 'Alterar senha',
        'button_text': 'Alterar',
        'link_text': link_text,
        'link_href': link_href
    }
    return render(request, template_name='auth/auth.html', context=context, status=200)