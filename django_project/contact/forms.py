from django import forms  
from .models import Contact
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ContactForm(forms.ModelForm):
    # email = forms.EmailField()
    class Meta:
        model = Contact
        fields = ["name","address","phone_no"]
        

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.PasswordInput()
    password2 =forms.PasswordInput()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
