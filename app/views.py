
<<<<<<< HEAD
=======
from django.shortcuts import render

>>>>>>> 7daf196bb735e9a7398ba8be92db94ed8883cbc3
# Create your views here.

from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request,soz):
    
    context = {
        "sozum":soz ,
<<<<<<< HEAD
        "ad": str('salam')
    }
    return render(request,'about.html',context)


=======
      
    }
    return render(request,'about.html',context =context)

def jed(request):
    c1 = {
        'meyve': 'banan',
    }
    return render(request,'index.html',context=c1,)
>>>>>>> 7daf196bb735e9a7398ba8be92db94ed8883cbc3

