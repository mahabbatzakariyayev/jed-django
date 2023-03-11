from django.db import models

# Create your models here.
class Article(models.Model):
   name= models.CharField("Ad", max_length=255)
   create_date= models.DateTimeField("yaranma tarixi",auto_now_add=True)

