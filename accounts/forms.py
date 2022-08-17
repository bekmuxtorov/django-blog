
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'region',)


class CustomUserChangeForms(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'password', 'last_name', 'email', 'region',)


