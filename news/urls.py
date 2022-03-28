from django.urls import path

from .views import main, get_category, view_news, add_news

urlpatterns = [
    path('', main, name='home'),
    path('category/<int:cat>/', get_category, name='category'),
    path('news/<int:news_id>/', view_news, name='view_news'),
    path('add_news/', add_news, name='add_news'),
]
