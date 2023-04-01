from django.urls import path
from . import views

urlpatterns = [
    path('register',views.registerW,name='register'),
    path('login',views.loginW,name='login'),
    path('logout',views.logoutW,name='logout')
]
