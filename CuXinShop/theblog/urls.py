from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detail_article/<int:id_article>', views.detail_article, name='detail_article'),
    path('detail_tag/<str:tag_name>', views.detail_tag, name='detail_tag'),
    path('list_article/', views.list_article, name='list_article'),
    path('list_tag/', views.list_tag, name='list_tag')
]
