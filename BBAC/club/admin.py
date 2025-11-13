from django.contrib import admin
from .models import *

# Register your models here.

# admin.site.register(Member)
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'role', 'joined_date')
    search_fields = ('name', 'email')
    list_filter = ('role',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'event_date', 'created_by')
    search_fields = ('event_date',)
    list_filter = ('title','location')

@admin.register(Participation)
class ParticipationAdmin(admin.ModelAdmin):
    list_display = ('member', 'event', 'attended', 'timestamp')
    list_filter = ('attended', 'event')
    search_fields = ('member_name', 'event_title')






