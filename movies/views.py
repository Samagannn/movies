from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.core.paginator import Paginator

from movies.filters import MovieFilter
from .models import Product, ProductImage, ProductAttribute, Category


class ProductView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'movie_list.html', {'movie_list': products})


def main(request):
    news = Product.objects.all().order_by('title')

    search = request.GET.get('search')
    if search:
        news = news.filter(title__icontains=search)

    filter_set = MovieFilter(request.GET, queryset=news)
    paginator = Paginator(filter_set.qs, 5)
    page = request.GET.get('page', 1)
    news = paginator.get_page(page)

    return render(request, 'index.html', {'news': news, 'filter': filter_set})


def item_detail(request, item_id):
    item = get_object_or_404(Product, pk=item_id)
    additional_images = item.images.exclude(is_primary=True)
    return render(request, 'index.html', {'item': item, 'additional_images': additional_images})


def detail_news(request, movie_id):
    # try:
    #     news = News.objects.get(id=id)
    # except News.DoesNotExist:
    #     raise Http404()

    news = get_object_or_404(Product, id=movie_id)
    return render(request, 'movie_list.html', {'news': news})


def news_by_category(request, id):
    category = get_object_or_404(Category, id=id)
    news = Product.objects.filter(category=category).order_by('-title')

    paginator = Paginator(news, 1)
    page = request.GET.get('page', 1)
    news = paginator.get_page(page)

    return render(request, 'index.html', {'news': news, 'category': category})

# Create your views here.
