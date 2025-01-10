from django.shortcuts import render, redirect

from django.views import generic
from ..models import Transaction, Customer
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import messages



class DetailView(generic.DetailView):
    model = Transaction
    template_name = "crm/detail.html"

def CustomerView(request, pk):
    if request.user.is_authenticated:
        transactions = Transaction.objects.filter(customer__id=pk)
        customer = Customer.objects.get(id=pk)
        return render(request, 'crm/customer_detail.html', {'transactions': transactions, 'customer': customer})
    else:
        messages.success(request, "You must be logged in to view this page.")
        return redirect('crm_app:home')
    
def TransactionView(request, pk):
    if request.user.is_authenticated:
        transaction = Transaction.objects.get(id=pk)
        return render(request, 'crm/transaction_detail.html', {'transaction': transaction})
    else:
        messages.success(request, "You must be logged in to view this page.")
        return redirect('crm_app:home')
        

class recent_orders_generic(generic.ListView):
    template_name = "crm/recent_orders.html"
    context_object_name = "latest_order_list"

    def get_queryset(self):
        return Transaction.objects.filter(transaction_datetime__lte=timezone.now()).order_by("transaction_datetime")[:5]