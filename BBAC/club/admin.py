from django.contrib import admin
from .models import *

# Register your models here.

# admin.site.register(Member)
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'role', 'joined_date')
    search_fields = ('name', 'email')
    list_filter = ('role',)
