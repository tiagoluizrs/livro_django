from django.urls import path, include
from medicSearch.views.AuthView import login_view, register_view, logout_view, recovery_view, change_password

urlpatterns = [
    path("login", login_view),
    path("register", register_view),
    path("logout", logout_view),
    path("recovery", recovery_view),
    path("change-password/<str:token>", change_password),
    path('social-auth/', include('social_django.urls', namespace="social")),
]