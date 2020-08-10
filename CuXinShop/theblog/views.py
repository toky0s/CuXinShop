from django.shortcuts import render
from django.shortcuts import HttpResponse


def home(request):
    return render(request, 'home.html', {})


def detail_article(request, id_article):
    return HttpResponse('Đây là bài viết số {}'.format(id_article))


def detail_tag(request, tag_name):
    return  HttpResponse('Đây là detail page của tag {}'.format(tag_name))


def list_article(request):
    return  HttpResponse('Đây là nơi hiển thị các bài viết mới nhất')


def list_tag(requests):
    return HttpResponse('Đây là nơi hiển thị các tag')