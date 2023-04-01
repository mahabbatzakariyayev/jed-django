
from django.shortcuts import get_object_or_404, redirect, render


from django.contrib import messages

# Create your views here.
from .models import Article
from django.shortcuts import render,HttpResponse
from .forms import ArticleForm
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
    print(articles)
    contextim  = {
        'articles': articles
    }
    return render(template_name='allarticles.html',request=request,context=contextim)
from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
def createarticle(request):
    form = ArticleForm( request.POST or None, request.FILES or None ) 

    if form.is_valid():
        name = form.cleaned_data.get('name')
        metn = form.cleaned_data.get('metn')
        sekil = form.cleaned_data.get("sekil")
        newArticle = Article(name= name,sekil=sekil,metn=metn)
        newArticle.author = request.user
        newArticle.save()
        

        messages.success(request,"Artikl ugurla yaradıldı")
        return redirect('index')
    
    context  = {
        'form' : form
    }
    return render(request,'createarticle.html',context)