from django.urls import path
from . import views
urlpatterns = [
   path('',views.index,name='index'),
   path('about/<str:soz>',views.about,name='about'),
   path('jed',views.jed),

]
