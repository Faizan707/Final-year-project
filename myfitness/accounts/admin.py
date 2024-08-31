# admin.py

from django.contrib import admin
from .models import CustomerAccounts, OtherAccounts

@admin.register(CustomerAccounts)
class CustomerAccountsAdmin(admin.ModelAdmin):
    list_display = ('name', 'customer_id', 'customer_fee', 'status')
    search_fields = ('name', 'customer_id')
    list_filter = ('status',)

@admin.register(OtherAccounts)
class OtherAccountsAdmin(admin.ModelAdmin):
    list_display = ('id', 'rent_fee', 'staff_fee', 'status')
    list_filter = ('status',)
