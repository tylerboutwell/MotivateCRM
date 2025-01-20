from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Customer, Transaction
from django.utils import timezone
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field

class AddCustomerForm(forms.ModelForm):
    first_name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "First Name", "class": "form-control",}),
        label="First Name",
        )
    
    last_name = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(attrs={"placeholder": "Last Name", "class": "form-control",}), 
        label="Last Name"
        )
    
    phone_number = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(attrs={"placeholder": "Phone Number", "class": "form-control",}), 
        label="Phone number"
        )
    
    email = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(attrs={"placeholder": "Email", "class": "form-control",}), 
        label="Email address"
        )
    
    address = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(attrs={"placeholder": "Address", "class": "form-control",}), 
        label="Address line"
        )
    
    city = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(attrs={"placeholder": "City", "class": "form-control",}), 
        label="City"
        )
    
    state = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(attrs={"placeholder": "State", "class": "form-control",}), 
        label="State"
        )
    
    postal_code = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(attrs={"placeholder": "Postal Code", "class": "form-control",}), 
        label="Postal Code",
        )
    

    class Meta:
        model = Customer
        exclude = ("user",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.helper.form_class= 'form-horizontal'
        self.helper.label_class='col-lg-1 badge align-self-center border-bottom border-secondary'
        self.helper.field_class = 'col-lg-9'
        self.helper.layout = Layout(
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'address',
            'city',
            'state',
            'postal_code',
            Submit('submit', 'Add Customer', css_class='btn d-block m-auto',)
        )

class AddTransactionForm(forms.ModelForm):
    customer = forms.ModelChoiceField(queryset=Customer.objects.all(), required=True,empty_label="-- Select Customer --", label="")
    total = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder": "Total", "class": "form-control"}), label="")
    transaction_datetime = forms.DateTimeField(required=True, widget=forms.widgets.DateTimeInput(attrs={"type": "datetime-local", "class": "form-control"}), initial=timezone.now(),label="")

    class Meta:
        model = Transaction
        exclude = ("user",)