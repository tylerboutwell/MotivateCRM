from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Customer, Transaction
from django.utils import timezone

class AddCustomerForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "First Name", "class": "form-control", 'style': 'width: 300px; display: inline',}), label="First Name",)
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Last Name", "class": "form-control", 'style': 'width: 300px; display: inline',}), label="Last Name")
    phone_number = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Phone Number", "class": "form-control", 'style': 'width: 300px; display: inline',}), label="Phone number")
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Email", "class": "form-control", 'style': 'width: 300px; display: inline'}), label="Email address")
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Address", "class": "form-control", 'style': 'width: 300px; display: inline'}), label="Address line")
    city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "City", "class": "form-control", 'style': 'width: 300px; display: inline'}), label="City")
    state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "State", "class": "form-control", 'style': 'width: 300px; display: inline'}), label="State")
    postal_code = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Postal Code", "class": "form-control", 'style': 'width: 300px; display: inline'}), label="Postal Code")

    class Meta:
        model = Customer
        exclude = ("user",)

class AddTransactionForm(forms.ModelForm):
    customer = forms.ModelChoiceField(queryset=Customer.objects.all(), required=True,empty_label="-- Select Customer --", label="")
    total = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder": "Total", "class": "form-control"}), label="")
    transaction_datetime = forms.DateTimeField(required=True, widget=forms.widgets.DateTimeInput(attrs={"type": "datetime-local", "class": "form-control"}), initial=timezone.now(),label="")

    class Meta:
        model = Transaction
        exclude = ("user",)