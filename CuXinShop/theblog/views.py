from django.shortcuts import HttpResponse, render, get_object_or_404, get_list_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from .models import Article, Tag
from django.views.generic import DetailView, ListView


def get_next_or_prev(models: object, item: Article, direction: str = 'next') -> object:
    getit = False
    if direction == 'prev':
        models = models.reverse()
    for m in models:
        if getit:
            return m
        if item == m:
            getit = True
    if getit:
        # This would happen when the last
        # item made getit True
        return models[0]
    return False


def home(request):
    return render(request, 'home.html', {})


def detail_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    article.view += 1
    article.save()
    models = Article.objects.all()
    next_article = get_next_or_prev(models, article)
    previous_article = get_next_or_prev(models, article, 'prev')
    return render(request,'view_detail_article.html', context={'article': article,'next_article': next_article, 'previous_article': previous_article})


def detail_tag(request, tag_name):
    tag = get_object_or_404(Tag, tag_name=tag_name)
    tag.view +=1
    tag.save()
    return render(request,'view_detail_tag.html', context={'tag':tag})


def list_article(request):
    articles = get_list_or_404(Article)
    return render(request, 'view_all_article.html', context={'articles':articles})


def list_tag(request):
    tags = Tag.objects.all()
    return render(request, 'view_all_tag.html', context={'tags':tags})


def list_article_with_tag(request, tag_name):
    tag = get_object_or_404(Tag, tag_name=tag_name)
    articles = tag.article_set.all()
    return render(request, 'view_list_article.html', context={'tag': tag, 'articles':articles})

def joke(request):
    return render(request, 'joke.html')

def profile(request):
    return HttpResponse('profile xin')
