from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404

from movies.models import Product


def login_required(login_url='/'):
    def inner_func_as_args(func):
        def inner_func(request, *args, **kwargs):
            if not request.user.is_authenticated:
                messages.warning(request, 'You should be authenticated!')
                return redirect(login_url)
            return func(request, *args, **kwargs)

        return inner_func

    return inner_func_as_args


def own_news(func):
    def inner_func(request, movie_id, *args, **kwargs):
        user = request.user
        movies = get_object_or_404(Product, id=movie_id)
        if user != movies.author:
            messages.warning(request, 'You cannot make any actions, it\'s not your movies.')
            return redirect('/news/main/')
        return func(request, movie_id, *args, **kwargs)

    return inner_func




