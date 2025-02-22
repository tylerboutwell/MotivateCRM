from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from ..models import Customer, Transaction
from ..forms import SignUpForm
from datetime import date
from django.db.models import Sum


def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username= username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in.")
            return redirect('crm_app:home')
        else:
            messages.success(request, "There was an error logging in. Please try again...")
            return redirect('crm_app:home')
    else:
        customers = Customer.objects.all().filter(user=request.user)
        transactions = Transaction.objects.all().filter(user=request.user)
        curr_month = date.today().strftime('%m')
        curr_year = date.today().strftime('%Y')
        transactions_curr_year = transactions.filter(transaction_datetime__year=curr_year)
        transactions_curr_month = transactions.filter(transaction_datetime__month=curr_month).filter(transaction_datetime__year=curr_year)
        month_sum = transactions_curr_month.aggregate(Sum("total", default=0))['total__sum']
        year_sum = transactions_curr_year.aggregate(Sum("total", default=0))['total__sum']
        context = {'customers':customers, 'transactions':transactions, 'transactions_curr_year':transactions_curr_year, 'transactions_curr_month':transactions_curr_month, 'month_sum':month_sum, 'year_sum':year_sum}
        return render(request, 'crm/home.html', context)

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('crm_app:home')

def Register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('crm_app:home')
    else:
        form = SignUpForm()
        return render(request, 'crm/register.html', {'form':form})
    return render(request, 'crm/register.html', {'form':form})
