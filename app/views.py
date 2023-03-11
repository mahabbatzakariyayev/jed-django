
# Create your views here.

from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request,soz):
    
    context = {
        "sozum":soz ,
        "ad": str('salam')
    }
    return render(request,'about.html',context)



