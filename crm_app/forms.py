from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Customer, Transaction
from django.utils import timezone

class AddCustomerForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Name", "class": "form-control"}), label="")
    phone_number = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Phone Number", "class": "form-control"}), label="")
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Email", "class": "form-control"}), label="")

    class Meta:
        model = Customer
        exclude = ("user",)

class AddTransactionForm(forms.ModelForm):
    customer = forms.ModelChoiceField(queryset=Customer.objects.all(), required=True,empty_label="--Select Customer--", label="")
    total = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder": "Total", "class": "form-control"}), label="")
    transaction_datetime = forms.DateTimeField(required=True, widget=forms.widgets.DateTimeInput(attrs={"type": "datetime-local", "class": "form-control"}), initial=timezone.now(),label="")

    class Meta:
        model = Transaction
        exclude = ("user",)