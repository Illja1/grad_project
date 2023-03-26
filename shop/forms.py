from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Furniture,Category


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='User name', widget = forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Password', widget = forms.PasswordInput(attrs={'class':'form-control'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='User name', help_text='User name must be 150 characters',widget = forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password', help_text='User name at least must be 8 characters and contains number and symbols',widget = forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm password',help_text='Password must match',widget = forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label="E-mail",widget = forms.EmailInput(attrs={'class':'form-control'}))


    class Meta:
        model = User
        fields = ('username', 'email', 'password1','password2')


class FurnitureForm(forms.ModelForm):
    class Meta:
        model = Furniture
        fields = ['name', 'description', 'characteristics', 'digital', 'price', 'photo', 'categories']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 10}),
            'characteristics': forms.Textarea(attrs={'cols': 80, 'rows': 10}),
            'categories': forms.CheckboxSelectMultiple(),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
