from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

# Create your views here.

def index(request):

    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
    }

    return render(request, 'main/index.html', context=context)
    
def about(request):
    context = {
        'title': 'About - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст о том, почему данный магазин очень крут и полезен для всех',
    }
    return render(request, 'main/about.html', context=context)
    