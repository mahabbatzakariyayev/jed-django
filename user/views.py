from django.http import HttpResponse
from django.shortcuts import redirect, render

from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate

from .forms import LoginForm, RegisterForm
# Create your views here.
def registerW(request):
    if request.method  == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():

            myusername = form.cleaned_data["username"]
            mypassword = form.cleaned_data["password"]
   
            newUser = User(username= myusername)
            newUser.set_password(mypassword)
            newUser.save()
            
            messages.success(request,"Istifadəçi uğurla yaradıldı")
            return redirect('index')
    
    else:
        form= RegisterForm()

    context = {
            "form":form
        }
    return render(request,'register.html',context)


def loginW(request):
    form = LoginForm(request.POST or None)
    context =  {'form': form}   
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')


        user = authenticate(username= username,password=password)
        
        if user is None:
            messages.error(request,'Istifadəçi adınız və ya şifrəniz yalnışdır')
            return render('login')

        login(request,user)
        messages.success(request, "Xoş gəlmişsiniz!")
        return redirect('index')
    

    return render(request,'login.html',context)