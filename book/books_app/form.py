from django import forms
from .models import Book
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title","author","published_date","isbn"]
        
        
class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.PasswordInput()
    password2 =forms.PasswordInput()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
