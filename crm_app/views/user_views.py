from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from ..models import Customer
from ..forms import SignUpForm

def home(request):
    customers = Customer.objects.all()
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
        return render(request, 'crm/home.html', {'customers':customers})

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
			return redirect('home')
    else:
		form = SignUpForm()
		return render(request, 'crm/register.html', {'form':form})

	return render(request, 'crm/register.html', {'form':form})
