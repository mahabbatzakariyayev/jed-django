from django.http import HttpResponse
from django.shortcuts import redirect, render

from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import login

from .forms import RegisterForm
# Create your views here.
def register(request):
    if request.method  == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():

            myusername = form.cleaned_data.get("username")
            mypassword = form.cleaned_data.get("password")
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



