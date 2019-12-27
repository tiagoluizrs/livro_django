from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    # fields = ('user','status',)
    list_display = ('user', 'status', 'role',)
    list_display_links = ('user', 'status', 'role',)
    list_filter = ('user', 'status', 'role',)
    ordering = ['created_at']
    search_fields = ['user__username']
    readonly_fields = ('created_at',)
    empty_value_display = 'unknown'

    # fieldsets = (
    #     (None, {
    #         'fields': ('user','status',)
    #     }),
    #     ('Advanced options', {
    #         'classes': ('wide', 'extrapretty'),
    #         'fields': ('role',),
    #     }),
    # )
    exclude = ('updated_at',)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Address)
admin.site.register(DayWeek)
admin.site.register(Rating)
admin.site.register(Speciality)
