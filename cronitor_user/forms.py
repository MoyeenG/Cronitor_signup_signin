from django import forms
from django.utils.safestring import mark_safe


class Signup(forms.Form):
    name = forms.CharField(label=mark_safe('Your Name: <br/>'), label_suffix="", widget=forms.TextInput(attrs={'placeholder': 'First Last'}), max_length=100)
    email = forms.CharField(label=mark_safe('Email: <br/>'), label_suffix="", widget=forms.EmailInput(attrs={'placeholder': 'example@work.com'}), max_length=100)
    password = forms.CharField(label=mark_safe('Password: <br/>'), label_suffix="", widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), max_length=20)


class Signin(forms.Form):
    email = forms.CharField(label=mark_safe('Email Address: <br/>'), label_suffix="", widget=forms.EmailInput, max_length=100)
    password = forms.CharField(label=mark_safe('Password: <br/>'), label_suffix="", widget=forms.PasswordInput, max_length=20)

