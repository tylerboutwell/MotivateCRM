from django.contrib import admin
from .models import Customer, Transaction

class CustomerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "phone_number", "email"]
    search_fields = ["phone_number", "email"]

class TransactionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["customer"]}),
        ("Customer Information", {"fields": ["transaction_datetime", "total"]})
        ]
    list_display = ["customer", "total", "transaction_datetime"]
    list_filter = ["transaction_datetime"]


admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Customer, CustomerAdmin)