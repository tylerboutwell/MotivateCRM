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
        widget=forms.widgets.EmailInput(attrs={"placeholder": "Email", "class": "form-control",}), 
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
        self.helper.label_class='col-lg-2 badge text-primary align-self-center border-bottom border-primary'
        self.helper.field_class = 'col-lg-9'
        self.helper.layout = Layout(
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'address',
            'city',
            'state',
            'postal_code'
        )

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))


	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	


class AddTransactionForm(forms.ModelForm):
    customer = forms.ModelChoiceField(queryset=Customer.objects.all(), required=True,empty_label="-- Select Customer --", label="")
    total = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder": "Total", "class": "form-control"}), label="")
    description = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Enter description here", "class": "form-control"}),label="")
    transaction_datetime = forms.DateTimeField(required=True, widget=forms.widgets.DateTimeInput(format='%Y-%m-%d %H:%M',attrs={"type": "datetime-local", "class": "form-control"}), initial=timezone.now(),label="")

    class Meta:
        model = Transaction
        exclude = ("user",)