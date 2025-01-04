from django.contrib import admin

from .models import Customer, Transaction

class TransactionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["customer"]}),
        ("Customer Information", {"fields": ["transaction_datetime", "total"]})
        ]


admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Customer)