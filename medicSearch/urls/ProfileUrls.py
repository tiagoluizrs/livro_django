from django.urls import path
from medicSearch.views.ProfileView import list_profile_view
from medicSearch.views.UserProfileView import edit_profile

urlpatterns = [
    path("", list_profile_view),
    path("<int:id>", list_profile_view),
    path("edit", edit_profile),
]