from django.urls import path, include
from medicSearch.views.AuthView import login_view, register_view, logout_view

urlpatterns = [
    path("login", login_view),
    path("register", register_view),
    path("logout", logout_view),
    path('social-auth/', include('social_django.urls', namespace="social")),
]