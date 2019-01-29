from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, help_text='Usuario de ingreso al sistema',
    	 widget=forms.TextInput(attrs={'class': "form-control"}),
    	 label = "Usuario")
    first_name = forms.CharField(max_length=30, required=True,
    	 widget=forms.TextInput(attrs={'class': "form-control"}),
    	 label = "Nombres")
    last_name = forms.CharField(max_length=30, required=True,
    	widget=forms.TextInput(attrs={'class': "form-control"}),
    	label = "Apellidos")
    email = forms.EmailField(max_length=254, help_text='Email Corporativo',
    	widget=forms.EmailInput(attrs={'class': "form-control"}),
    	label = "Correo Electronico")
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control"}),
        help_text=("Vuelva a escribir la contraseña para confirmación"))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        labels = {
        	'username': 'Username',
        	'first_name' :'Nombres',
        	'last_name' : 'Apelldios',
        	'email' : 'Correo Electrónico Interno',
        }
