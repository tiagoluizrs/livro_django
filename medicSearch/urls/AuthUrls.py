from django.urls import path, include
from medicSearch.views.AuthView import login_view, register_view, logout_view, recovery_view, change_password

urlpatterns = [
    path("login", login_view, name='login'),
    path("register", register_view, name='register'),
    path("logout", logout_view, name='logout'),
    path("recovery", recovery_view, name='recovery'),
    path("change-password/<str:token>", change_password, name='change-password'),
    path('social-auth/', include('social_django.urls', namespace="social")),
]