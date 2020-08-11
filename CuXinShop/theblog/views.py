from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import Http404
from .models import Article, Tag
from django.views.generic import DetailView, ListView


def home(request):
    return render(request, 'home.html', {})


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article.html'


def detail_article(request, id_article):
    return HttpResponse('Đây là bài viết số {}'.format(id_article))


def detail_tag(request, tag_name):
    return  HttpResponse('Đây là detail page của tag {}'.format(tag_name))


def list_article(request):
    return  HttpResponse('Đây là nơi hiển thị các bài viết mới nhất')


def list_tag(request):
    return HttpResponse('Đây là nơi hiển thị các tag')


def list_article_with_tag(request, tag_name: str):
    if len(Tag.objects.all().filter(tag_name=tag_name)) == 0:
        return Http404('ko tim thay trang nay')
    else:
        tag = Tag.objects.all().filter(tag_name=tag_name)[0]
        articles = tag.article_set.all()

    return render(request, 'tag.html', context={'tag': tag,'articles':articles})
