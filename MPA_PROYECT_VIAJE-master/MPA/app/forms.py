from django import forms
from .models import Ciudad
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

class CiudadForm(forms.ModelForm):
    class Meta:
        model = Ciudad
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm): 

    class Meta: 
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"] 