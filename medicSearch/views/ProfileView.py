from django.shortcuts import render, redirect
from medicSearch.models import Profile
from django.core.paginator import Paginator

def list_profile_view(request, id=None):
    profile = None
    if id is None and request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user).first()
    elif id is not None and request.user.is_authenticated:
        profile = Profile.objects.filter(user__id=id).first()
    elif not request.user.is_authenticated:
        return redirect(to='/')

    favorites = profile.favorites.all()
    if len(favorites) > 0:
        paginator = Paginator(favorites, 8)
        page = request.GET.get('page')
        favorites = paginator.get_page(page)

    context = {
        'profile': profile,
        'favorites': favorites
    }

    return render(request, template_name='profile/profile.html', context=context, status=200)