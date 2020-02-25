from django.urls import path
from medicSearch.views.HomeView import home_view

urlpatterns = [
    path("", home_view),
]