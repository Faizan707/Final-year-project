from django.contrib import admin
from .models import Assistant

@admin.register(Assistant)
class AssistantAdmin(admin.ModelAdmin):
    list_display = ( 'assistantID','name',   'phone_number', 'qualification', 'experience', 'available_from', 'available_to')
    search_fields = ('name',  'phone_number')
