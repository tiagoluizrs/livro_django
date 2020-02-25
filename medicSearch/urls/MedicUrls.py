from django.urls import path
from medicSearch.views.MedicView import list_medics_view, list_medic_view

urlpatterns = [
    path("", list_medics_view),
    path("<int:id>", list_medic_view),
]