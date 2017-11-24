from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from menu.models import *

class SigninForm(UserCreationForm):

	class Meta:
		model = User
		fields = [
				'username',
				'first_name',
				'last_name',
				'email',
				'password1',
				'password2',
		]
		labels = {
				'username':'Usuario',
				'first_name':'Nombre',
				'last_name':'Apellido',
				'email':'Correo',
		}

class BookingForm(forms.ModelForm):

    class Meta:
    	model=Book

    	fields = [
    		'name',
    		'telephone',
    		'email',
    		'date',
    		'time',
    		'people',
    		'comments'
    	]

    	widgets = {
			'name':forms.TextInput(attrs={'class':'form-control'}),
			'telephone':forms.TextInput(attrs={'class':'form-control'}),
			'email':forms.EmailInput(attrs={'class':'form-control'}),
			'date':forms.TextInput(attrs={'class':'form-control'}),
			'time':forms.TextInput(attrs={'class':'form-control'}),
			'people':forms.TextInput(attrs={'class':'form-control', 'type':'number', 'min':1, 'max':10}),
			'comments':forms.Textarea(attrs={'class':'form-control','rows':2}),
		}

class OrderForm(forms.ModelForm):
	class Meta:
		model = Order

		fields = [
			'table',
			'dish',
			'quantity',
		]

		widgets = {
			'quantity':forms.TextInput(attrs={'class':'form-control', 'type':'number', 'min':1, 'max':10}),
		}

class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customers
		fields = ['idNumber', 'name', 'last_name','table']
		labels = {'idNumber':'ID Number','name':'First Name','last_name':'Last Name','table':'Table'}

class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
