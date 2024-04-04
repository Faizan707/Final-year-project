from django.contrib import admin
from .models import Manager

class ManagerAdmin(admin.ModelAdmin):
    list_display = ('name', 'password')  # Display fields in admin interface

admin.site.register(Manager, ManagerAdmin)
