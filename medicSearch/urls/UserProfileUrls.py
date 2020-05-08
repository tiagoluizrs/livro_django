from django.urls import path
from medicSearch.views.UserProfileView import edit_profile

urlpatterns = [
    path("", edit_profile),
]