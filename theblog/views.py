from django.shortcuts import HttpResponse, render, get_object_or_404, Http404
from .models import Article, Tag


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


def get_object_with_view_highest(objects):
    result = None
    view = 0
    for object in objects:
        view_tem = object.view
        if view_tem > view:
            result = object
    return result

def home(request):
    return render(request, 'home.html')


def detail_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    article.view += 1
    article.save()
    models = Article.objects.all()

    tag_with_view_highest = get_object_with_view_highest(article.tags.all())
    next_article = get_next_or_prev(models, article)
    previous_article = get_next_or_prev(models, article, 'prev')

    context = {'article': article,
               'next_article': next_article,
               'previous_article': previous_article,
               'tag_with_view_highest': tag_with_view_highest}

    return render(request,'view_detail_article.html', context=context)


def detail_tag(request, tag_name):
    tag = get_object_or_404(Tag, tag_name=tag_name)
    tag.view +=1
    tag.save()
    return render(request,'view_detail_tag.html', context={'tag':tag})


def list_article(request):
    articles = Article.objects.all()
    if articles.count() == 0:
        return Http404()

    class AllTag:
        tag_name = 'all'
        tag_full_name = 'Tất cả'
    tag = AllTag()
    return render(request, 'view_list_article.html', context={'tag': tag, 'articles':articles})


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
    return render(request, 'profile.html')
