from django.shortcuts import HttpResponse, render, get_object_or_404, get_list_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from .models import Article, Tag
from django.views.generic import DetailView, ListView


def home(request):
    return render(request, 'home.html', {})


def detail_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    article.view += 1
    article.save()
    return render(request,'article.html', context={'article': article})


def detail_tag(request, tag_name):
    return  HttpResponse('Đây là detail page của tag {}'.format(tag_name))


def list_article(request):
    articles = get_list_or_404(Article)
    return render(request, 'view_all_article.html', context={'articles':articles})


def list_tag(request):
    return HttpResponse('Đây là nơi hiển thị các tag')


def list_article_with_tag(request, tag_name):
    try:
        tag = Tag.objects.get(tag_name=tag_name)
        articles = tag.article_set.all()
    except ObjectDoesNotExist:
        return Http404('ko ton tai trang nay')
    return render(request, 'view_list_article.html', context={'tag': tag, 'articles':articles})

