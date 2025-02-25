from django.shortcuts import render, redirect

from django.views import generic
from ..models import Transaction, Customer
from django.utils import timezone
from django.contrib import messages
from ..forms import AddCustomerForm, AddTransactionForm
from django.contrib.auth.decorators import permission_required
from django.db.models import Q

def CustomerView(request, pk):
    if request.user.is_authenticated:
        transactions = Transaction.objects.filter(customer__id=pk)
        customer = Customer.objects.get(id=pk)
        if customer.user == request.user:
            context = {'transactions': transactions, 'customer': customer}
            return render(request, 'crm/customer_detail.html', context)
        else:
            messages.success(request, "You do not have permission to view this customer.")
            return redirect('crm_app:home')
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
        if transaction.user == request.user:
            return render(request, 'crm/transaction_detail.html', {'transaction': transaction})
        else:
            messages.success(request, "You do not have permission to view this transaction.")
            return redirect('crm_app:home')
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
    customers = Customer.objects.all().filter(user=request.user)
    if request.user.is_authenticated:
        return render(request, 'crm/customers.html', {'customers':customers})
    else:
        messages.success(request, "You must be logged in to view this page.")
        return redirect('crm_app:home')
    
def transactions(request):
    transactions = Transaction.objects.all().filter(user=request.user)
    if request.user.is_authenticated:
        return render(request, 'crm/transactions.html', {'transactions':transactions})
    else:
        messages.success(request, "You must be logged in to view this page.")
        return redirect('crm_app:home')
    
def DeleteCustomer(request, pk):
    if request.user.is_authenticated:
        customer = Customer.objects.get(id=pk)
        if request.method == "DELETE":
            customer.delete()
            messages.success(request, "Customer has been deleted")
            customers = Customer.objects.all().filter(user=request.user)
            return render(request, 'crm/customers.html', {'customers': customers})
        return render(request, 'crm/partials/delete_customer.html', {'customer': customer})
    else:
        messages.success(request, "You must be logged in to delete data.")
        return redirect('crm_app:customers')
    
def DeleteTransaction(request, pk):
    if request.user.is_authenticated:
        transaction = Transaction.objects.get(id=pk)
        if request.method == "DELETE":
            messages.success(request, "Transaction has been deleted")
            transaction.delete()
            transactions = Transaction.objects.all().filter(user=request.user)
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
                        add_customer = form.save(commit=False)
                        add_customer.user = request.user
                        add_customer.save()
                        messages.success(request, "Customer successfully added.")
                        return redirect('crm_app:customers')
            return render(request, 'crm/add_customer.html', {'form': form})
    else:
        messages.success(request, "You must be logged in to add a customer.")
        return redirect('crm_app:home')
    
def AddTransaction(request):
    form = AddTransactionForm(request.POST or None)
    form.fields['customer'].queryset = Customer.objects.all().filter(user=request.user)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_transaction = form.save(commit=False)
                add_transaction.user = request.user
                add_transaction.save()
                messages.success(request, "Transaction successfully added.")
                return redirect('crm_app:transactions')
        return render(request, 'crm/add_transaction.html', {'form': form})
    else:
        messages.success(request, "You must be logged in to add a transaction.")
        return redirect('crm_app:home')
    
def SearchCustomer(request):
    if request.user.is_authenticated:
        customers = Customer.objects.all().filter(user=request.user)
        searchstr = request.POST.get('search')
        if searchstr:
            results = customers = customers.filter(Q(first_name__contains=searchstr) | Q(last_name__contains=searchstr))
        else:
            results = Customer.objects.all().filter(user=request.user)
        return render(request, 'crm/partials/search_customer.html', {'customers': results})
        
    else: 
        messages.success(request, "You must be logged in to search customers.")
        return redirect('crm_app:home')