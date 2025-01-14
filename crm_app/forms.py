from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Customer, Transaction

class AddCustomerForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Name", "class": "form-control"}), label="")
    phone_number = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Phone Number", "class": "form-control"}), label="")
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Email", "class": "form-control"}), label="")

    class Meta:
        model = Customer
        exclude = ("user",)

class AddTransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        exclude = ("user",)