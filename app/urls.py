from django.urls import path
from .views import index, myabout

urlpatterns = [
    path("", index),
     path("aboutt", myabout),
]
