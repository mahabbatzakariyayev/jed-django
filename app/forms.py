from django import forms
from app.models import Article


# class ArticleForm(forms.ModelForm):

#     class Meta:
#         model = Article
#         fields = ("name","metn")

class ArticleForm(forms.Form):
    name = forms.TextInput()
    metn = forms.TextInput()

