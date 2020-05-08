from django.urls import path
from medicSearch.views.AuthView import login_view, register_view

urlpatterns = [
    path("login", login_view),
    path("register", register_view),
]