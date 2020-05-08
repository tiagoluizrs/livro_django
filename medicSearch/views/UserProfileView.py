from django.shortcuts import render, redirect, get_object_or_404
from medicSearch.models import Profile
from medicSearch.forms.UserProfileForm import UserProfileForm, UserForm

def edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    message = None

    if request.method == 'POST':
        profileForm = UserProfileForm(request.POST, request.FILES,instance=profile)
        userForm = UserForm(request.POST, instance=request.user)
    else:
        profileForm = UserProfileForm(instance=profile)
        userForm = UserForm(instance=request.user)

    if profileForm.is_valid() and userForm.is_valid():
        profileForm.save()
        userForm.save()
        message = { 'type': 'success', 'text': 'Dados atualizados com sucesso' }
    else:
        if request.method == 'POST':
            message = { 'type': 'danger', 'text': 'Dados inválidos' }

    context = {
        'profileForm': profileForm,
        'userForm': userForm,
        'message': message
    }

    return render(request, template_name='user/profile.html', context=context, status=200)