<<<<<<< HEAD

=======
>>>>>>> 7daf196bb735e9a7398ba8be92db94ed8883cbc3
from django.urls import path
from . import views
urlpatterns = [
   path('',views.index,name='index'),
   path('about/<str:soz>',views.about,name='about'),
<<<<<<< HEAD
=======
   path('jed',views.jed),
>>>>>>> 7daf196bb735e9a7398ba8be92db94ed8883cbc3

]
