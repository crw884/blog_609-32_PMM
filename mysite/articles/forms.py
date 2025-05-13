from django import forms

from . import models

class ArticleForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'body', 'thumbnail']
        labels = {
            'title': 'Title',
            'body': 'Text',
            'thumbnail': 'Thumbnail',
        }
        widgets = {
            "title": forms.TextInput(attrs={'placeholder' : 'Напишите название статьи','class': 'form-control mb-3 article_text-title'}),
            "body": forms.Textarea(attrs={'placeholder': 'Напишите текст статьи','class': 'form-control mb-3 article_text-body'}),
            "thumbnail": forms.ClearableFileInput(attrs={'class': 'form-control mb-3'}),
        }
    