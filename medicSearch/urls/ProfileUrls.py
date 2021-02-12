from django.urls import path
from medicSearch.views.ProfileView import list_profile_view, edit_profile

# Adicione o atributo `name` e o valor as linhas a seguir:
urlpatterns = [
    path("", list_profile_view, name='profiles'),
    path("<int:id>", list_profile_view, name='profile'),
    path("edit", edit_profile, name='edit-profile'),
]