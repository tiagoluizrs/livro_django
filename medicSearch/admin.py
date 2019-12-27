from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialtiesList', 'addressesList',)

    def specialtiesList(self, obj):
        listSpecialties = []
        for i in obj.specialties.all():
            listSpecialties.append(i.name)
        return listSpecialties

    def addressesList(self, obj):
        return [i.name for i in obj.addresses.all()]

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Address)
admin.site.register(DayWeek)
admin.site.register(Rating)
admin.site.register(Speciality)
