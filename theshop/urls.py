from django.urls import path, include
from . import views

app_name = 'theshop'
urlpatterns = [
    path('all_item', include(views.all_item), name='all_item'),
]