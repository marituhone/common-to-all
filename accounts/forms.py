from django import forms 
from django.forms import ModelForm
from django.forms import Form
from django.contrib.auth.forms import UserChangeForm 
from accounts.models import *

class ListForm(ModelForm):
    class Meta:
        model = CustomUser
        fields =('fullname','email','phone','profile_pic')

            
class RegistrationForm(forms.Form):
    fullname = forms.CharField(label="fullname",max_length=30,widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class":"form-control"}))
    password = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput(attrs={"class":"form-control"}))
    phone= forms.CharField(label="phone_number",widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))   
    profile_pic = forms.FileField(label="profile_pic",required=False,widget=forms.FileInput(attrs={"class":"form-control"}))
    