from django.http import HttpResponse

def list_profile_view(request, id=None):
    if id is None:
        id = request.user.id

    print(request.user.username)
    print(request.user.email)
    print(request.user.first_name)
    print(request.user.last_name)
    print(request.user.date_joined)
    print(request.user.is_active)
    print(request.user.is_superuser)
    return HttpResponse('<h1>Usuário de id %s!</h1>' % id)