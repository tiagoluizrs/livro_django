from django.urls import path
from medicSearch.views.AuthView import login

urlpatterns = [
    path("login", login),
]