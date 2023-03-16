
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from app.forms import ArticleForm

# Create your views here.
from .models import Article
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

def showarticle(request,id):
    # article = get_object_or_404(Article,id=id)
    article = Article.objects.get(id=id)
    context ={
        'article': article
    }
    print(article)
    return render(request,'article.html',context=context)

def allarticles(request):
    articles = Article.objects.all()
    contextim  = {
        'articles': articles
    }
    return render(template_name='allarticles.html',request=request,context=contextim)

def createarticle(request):
    form = ArticleForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request,"Artikl ugurla yadda saxlanildi")
        return redirect('index')
    context = {
        'form': form
    }
    return render(request,"createarticle.html",context)
