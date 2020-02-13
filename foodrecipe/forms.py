from django import forms
from django.contrib.auth.models import User
from .models import fooddetail

class addForm(forms.ModelForm):

    class Meta:
        model = fooddetail
        fields = ('name', 'description','ingredients','steps','image')

class RegForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(widget=forms.EmailInput)
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password']

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','password']



