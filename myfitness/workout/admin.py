from django.contrib import admin
from .models import Workouts

def workouts_admin(modeladmin, request, queryset):
    for obj in queryset:
        print(obj.customer_id, obj.day, obj.workout_name, obj.exercises)

workouts_admin.short_description = "Display Workouts"

def register_workouts_admin():
    admin.site.register(Workouts, list_display=('customer_id', 'day', 'workout_name', 'exercises'),
                        search_fields=('customer_id', 'day', 'workout_name'),
                        list_filter=('day', 'workout_name'),
                        actions=[workouts_admin])

register_workouts_admin()
