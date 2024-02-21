from django.contrib import admin
from .models import *

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['id','customer_name']



@admin.register(InvoiceDetails)
class InvoiceDetailsAdmin(admin.ModelAdmin):
    list_display = ['id','invoice','description','quantity','unit_price','price']