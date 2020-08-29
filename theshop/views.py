from django.shortcuts import render, HttpResponse, Http404
from django.contrib.auth.decorators import login_required


# Create your views here.
def all_item(request):
    return HttpResponse('All_item')


def detail_item(request):
    return HttpResponse('Detail item')


def add_to_cart(request):
    return HttpResponse('Add to cart')


@login_required
def buy_item(request):
    return HttpResponse('Buy item')