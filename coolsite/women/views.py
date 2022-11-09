from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render
from women.models import *

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}
        ]


def index(request):
    posts = Women.objects.all()
    cats = Category.objects.all()
    context = {
        'menu': menu,
        'title': 'Главная страница',
        'posts': posts,
        'cats': cats,
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=context)


def about(request):
    return render(request, 'women/about.html', {'title': 'О нас', 'menu': menu})


def addpage(request):
    return HttpResponse('Добавить статью')


def contact(request):
    return HttpResponse('Наши контакты')


def login(request):
    return HttpResponse('Вход')


def show_post(request, post_id):
    return HttpResponse(post_id)


def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'menu': menu,
        'title': 'Главная страница',
        'posts': posts,
        'cats': cats,
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h>')