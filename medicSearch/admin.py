from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('user', 'status', 'role','specialtiesList', 'addressesList',)
    list_filter = ('status', 'role',)
    search_fields = ['user__username']
    readonly_fields = ('created_at',)
    empty_value_display = '--vazio--'
    exclude = ('created_at', 'updated_at',)

    def specialtiesList(self, obj):
        return [i.name for i in obj.specialties.all()]

    def addressesList(self, obj):
        return [i.name for i in obj.addresses.all()]

admin.site.register(Profile, ProfileAdmin)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Neighborhood)
admin.site.register(Address)
admin.site.register(DayWeek)
admin.site.register(Rating)
admin.site.register(Speciality)
