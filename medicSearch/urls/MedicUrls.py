from django.urls import path
from medicSearch.views.MedicView import list_medics_view, add_favorite_view, remove_favorite_view, rate_medic

urlpatterns = [
    path("", list_medics_view),
    path("favorite", add_favorite_view),
    path("favorite/remove", remove_favorite_view),
    path("rating/<int:medic_id>", rate_medic),
]