from django.contrib.admin.utils import get_model_from_relation
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render
from articles.models import Article

def homepage(request):
    articles = Article.objects.all().order_by('-date')[:3]
    data = {"info": {"header": "Главная", "message":"Последние статьи"}, "articles": articles}
    return render(request, 'homepage.html', context=data,)

def about(request):
    header = "О нас"
    staff = ['Я']
    director = {"name": "Прокопий Харитонов", "img": "/director.png"}
    address = ('Пр. Пролетарский 7/8','Сургут', 'Россия')
    data = {"address": address, "header": header, "staff": staff, "director": director}
    return render(request, 'about.html', data)

