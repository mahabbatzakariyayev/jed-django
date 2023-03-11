


# Create your views here.

from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request,soz):
    
    context = {
        "sozum":soz ,
      
    }
    return render(request,'about.html',context =context)

def jed(request):
    c1 = {
        'meyve': 'banan',
    }
    return render(request,'index.html',context=c1,)

