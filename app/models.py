from django.db import models

# Create your models here.



class Article(models.Model):
    author = models.ForeignKey("auth.User", verbose_name=("Yaradan"), on_delete=models.CASCADE)
    sekil = models.ImageField(("Sekil"), upload_to="images/", height_field=None, width_field=None, max_length=None)
    name =models.CharField("Ad",max_length=255)
    metn = models.TextField(verbose_name="metn")
    create_date = models.DateTimeField('Yaranma tarixi',auto_now_add=True)
