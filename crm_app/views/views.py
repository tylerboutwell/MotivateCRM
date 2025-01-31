from django.shortcuts import render, redirect

from django.views import generic
from ..models import Transaction, Customer
from django.utils import timezone
from django.contrib import messages
from ..forms import AddCustomerForm, AddTransactionForm
from django.http import QueryDict



class DetailView(generic.DetailView):
    model = Transaction
    template_name = "crm/detail.html"

def CustomerView(request, pk):
    if request.user.is_authenticated:
        transactions = Transaction.objects.filter(customer__id=pk)
        customer = Customer.objects.get(id=pk)
        context = {'transactions': transactions, 'customer': customer}
        return render(request, 'crm/customer_detail.html', context)
    else:
        messages.success(request, "You must be logged in to view this page.")
        return redirect('crm_app:home')

def UpdateCustomerView(request, pk):
    if request.user.is_authenticated:
        customer = Customer.objects.get(id=pk)
        form = AddCustomerForm(request.POST or None, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer successfully updated.")
            return render(request, 'crm/customer_detail.html', {'customer': customer})
        return render(request, 'crm/partials/update_customer.html', {'form': form, 'customer': customer})
    else:
        messages.success(request, "You must be logged in to add a customer.")
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
    
def UpdateTransactionView(request, pk):
    if request.user.is_authenticated:
        transaction = Transaction.objects.get(id=pk)
        form = AddTransactionForm(request.POST or None, instance=transaction)
        if form.is_valid():
            form.save()
            messages.success(request, "Transaction successfully updated.")
            return render(request, 'crm/transaction_detail.html', {'transaction': transaction})
        return render(request, 'crm/partials/update_transaction.html', {'form': form, 'transaction': transaction})
    else: 
        messages.success(request, "You must be logged in to add a customer.")
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
        return redirect('crm_app:customers')
    
def DeleteTransaction(request, pk):
    if request.user.is_authenticated:
        transaction = Transaction.objects.get(id=pk)
        if request.method == "DELETE":
            messages.success(request, "Transaction has been deleted")
            transaction.delete()
            transactions = Transaction.objects.all() 
            return render(request, 'crm/transactions.html', {'transactions': transactions})    
        return render(request, 'crm/partials/delete_transaction.html', {'transaction': transaction})
    else:
        messages.success(request, "You must be logged in to delete data.")
        return redirect('crm_app:home')
    
def AddCustomer(request):
    form = AddCustomerForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_customer = form.save()
                messages.success(request, "Customer successfully added.")
                return redirect('crm_app:customers')
        return render(request, 'crm/add_customer.html', {'form': form})
    else:
        messages.success(request, "You must be logged in to add a customer.")
        return redirect('crm_app:home')
    
def AddTransaction(request):
    form = AddTransactionForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_transaction = form.save()
                messages.success(request, "Transaction successfully added.")
                return redirect('crm_app:transactions')
        return render(request, 'crm/add_transaction.html', {'form': form})
    else:
        messages.success(request, "You must be logged in to add a transaction.")
        return redirect('crm_app:home')