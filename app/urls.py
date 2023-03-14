from django.urls import path
from . import views
urlpatterns = [
   path('',views.index,name='index'),
   path('about/<str:soz>',views.about,name='about'),
   path('jed',views.jed,name='jed'),
   path('article/<int:id>',views.showarticle,name = 'article'),
   path('allarticles',views.allarticles,name = 'allarticles'),
   path('create',views.createarticle,name='createarticle')
]
