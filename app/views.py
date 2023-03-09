from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request,soz):
    soz1 = soz
    context = {
        "sozum":soz1
    }
    return render(request,'about.html',context)