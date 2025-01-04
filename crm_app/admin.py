from django.contrib import admin

from .models import Customer, Transaction

class TransactionAdmin(admin.ModelAdmin):
    fields = ["customer", "transaction_datetime", "total"]


admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Customer)