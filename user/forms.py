from django import forms
from django.contrib.auth.models  import User
class RegisterForm(forms.Form):


    username = forms.CharField(max_length=32,label="Username")
    password = forms.CharField(max_length=64,label="Password",widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=64,label="Password Again",widget=forms.PasswordInput())

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")

        if password and password2  and password != password2:
            raise forms.ValidationError("Parollar Eyni Deyil")
        
        values ={
            "username" : username,
            "password" : password

        }
        return values


           
class LoginForm(forms.Form):
    username = forms.CharField(max_length=32,label='Username')
    password = forms.CharField(max_length=64,label='Password',widget=forms.PasswordInput())



