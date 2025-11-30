from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'DarkMoon - главная',
        'content': 'Магазин милового мерча'
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'DarkMoon - О нас (не ононас)',
        'content': 'Ононас',
        'text_on_page': 'Ононасов нет тут'
    }
    return render(request, 'main/about.html', context)
