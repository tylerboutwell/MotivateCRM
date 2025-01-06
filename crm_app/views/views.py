from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.views import generic
from ..models import Transaction, Customer
from django.utils import timezone



class DetailView(generic.DetailView):
    model = Transaction
    template_name = "crm/detail.html"

class CustomerDetailView(generic.DetailView):
    model = Customer
    template_name = "crm/customer_detail.html"

class recent_orders_generic(generic.ListView):
    template_name = "crm/recent_orders.html"
    context_object_name = "latest_order_list"

    def get_queryset(self):
        return Transaction.objects.filter(transaction_datetime__lte=timezone.now()).order_by("transaction_datetime")[:5]