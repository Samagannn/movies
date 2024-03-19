from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.core.paginator import Paginator
from .models import Product, ProductImage, ProductAttribute


class ProductView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'movies/movie_list.html', {'movie_list': products})


def main(request):

    news = Product.objects.all()

    search = request.GET.get('search')
    if search:
        news = news.filter(title__icontains=search)

    paginator = Paginator(news, 4)
    page = request.GET.get('page', 1)
    news = paginator.get_page(page)

    return render(request, 'movies/index.html', {'news': news})



def item_detail(request, item_id):
    item = get_object_or_404(Product, pk=item_id)
    additional_images = item.images.exclude(is_primary=True)
    return render(request, 'movies/index.html', {'item': item, 'additional_images': additional_images})

def detail_news(request, movie_id):
    # try:
    #     news = News.objects.get(id=id)
    # except News.DoesNotExist:
    #     raise Http404()

    news = get_object_or_404(Product, id=movie_id)
    return render(request, 'movies/movie_list.html', {'news': news})
# Create your views here.
