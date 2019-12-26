from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Address)
admin.site.register(DayWeek)
admin.site.register(Rating)
admin.site.register(Speciality)
