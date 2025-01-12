from django.shortcuts import render, redirect

from django.views import generic
from ..models import Transaction, Customer
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import messages
from ..forms import AddCustomerForm



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
    
def CustomerTransactionsView(request, pk):
    if request.user.is_authenticated:
        transactions = Transaction.objects.filter(customer__id=pk)
        customer = Customer.objects.get(id=pk)
        return render(request, 'crm/customer_transactions.html', {'transactions': transactions, 'customer': customer})
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
        
def Customers(request):
    customers = Customer.objects.all()
    if request.user.is_authenticated:
        return render(request, 'crm/customers.html', {'customers':customers})
    else:
        messages.success(request, "You must be logged in to view this page.")
        return redirect('crm_app:home')
    
class transactions(generic.ListView):
    template_name = "crm/transactions.html"
    context_object_name = "transactions"

    def get_queryset(self):
        return Transaction.objects.filter(transaction_datetime__lte=timezone.now()).order_by("-transaction_datetime")
    
def DeleteCustomer(request, pk):
    if request.user.is_authenticated:
        customer = Customer.objects.get(id=pk)
        customer.delete()
        messages.success(request, "Customer has been deleted")
        return redirect('crm_app:home')
    else:
        messages.success(request, "You must be logged in to delete data.")
        return redirect('crm_app:home')