from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from medicSearch.forms.AuthForm import LoginForm

def login(request):
    loginForm = LoginForm()
    message = None

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        loginForm = LoginForm(request.POST)

        if loginForm.is_valid():
            user = authenticate(username=username, password=password)
            if user is not None:
                return redirect('/')
            else:
                message = {
                    'type': 'danger',
                    'text': 'Dados de usuário incorretos'
                }

    context = {
        'loginForm': loginForm,
        'message': message
    }
    return render(request, template_name='auth/login.html', context=context, status=200)