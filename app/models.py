from django.db import models

# Create your models here.
class Article(models.Model):
    
    name =models.CharField("Ad",max_length=255)
    metn = models.TextField(verbose_name="metn")
    create_date = models.DateTimeField('Yaranma tarixi',auto_now_add=True)
