from django.shortcuts import render, get_object_or_404, redirect

from .models import News, Category
from .forms import NewsForm


def main(request):
    news = News.objects.all()
    categories = Category.objects.all()
    context = {
        "news": news,
        "title": "Список квартиры",
        "categories": categories,
    }
    return render(request, 'news/index.html', context)


def get_category(request, cat):
    news = News.objects.filter(category=cat)
    categories = Category.objects.all()
    category = Category.objects.get(pk=cat)
    context = {
        "news": news,
        "categories": categories,
        "category": category,
    }
    return render(request, 'news/category.html', context)


def view_news(request, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)  # Получает один конкретный объект если получает больше или менше одного просает 404
    return render(request, 'news/view_news.html', {"news_item": news_item})


def add_news(request):
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save()
            return redirect(news)
    else:
        form = NewsForm()
    context = {
        "title": "Добовить данные",
        "form": form,
    }
    return render(request, 'news/add_news.html', context)


