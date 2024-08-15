from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email")
        
        
class LoginForm(forms.Form):
    email = forms.EmailField(
        max_length=120, widget=forms.EmailInput(
            attrs={'class': 'myfieldclass'}
        )
    )
    password = forms.CharField(
        max_length=150, widget=forms.PasswordInput(
            attrs={'class': 'myfieldclass'}
        )
    )
    
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email")