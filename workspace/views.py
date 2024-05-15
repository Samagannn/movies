from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout

from movies.filters import MovieFilter
from workspace.decarators import login_required, own_news
from movies.models import Product, Category, Tag, ProductImage
from workspace.forms import MovieForm, LoginForm, RegisterForm, ChangeProfileForm, ChangePasswordForm


@login_required(login_url='/auth/login/')
def workspace(request):
    news = Product.objects.all().order_by('title')
    if request.user.is_authenticated:
        news = Product.objects.filter(author=request.user)

    search = request.GET.get('search')
    if search:
        news = news.filter(title__icontains=search)

    filter_set = MovieFilter(request.GET, queryset=news)

    paginator = Paginator(filter_set.qs, 4)
    page = int(request.GET.get('page', 1))
    news = paginator.get_page(page)

    return render(request, 'workspace/index.html', {'news': news, 'filter': filter_set})


@login_required()
def create_movies(request):
    form = MovieForm()

    if request.method == 'POST':
        form = MovieForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.save()
            messages.success(request, f'A movie by name "{news.title}" was created."')

            return redirect('/news/main/')
        messages.error(request, f'Correct errors below')

    return render(request, 'workspace/create_movies.html', {'form': form})


@login_required()
@own_news
def update_movies(request, movie_id):
    movie = get_object_or_404(Product, id=movie_id)

    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            news = form.save()
            messages.error(request, f'The movie "{movie.title}" was updated."')
            return redirect('/news/main/')
        messages.error(request, f'Correct errors below')
    else:
        form = MovieForm(instance=movie)

    return render(request, 'workspace/update_movies.html',
                  {'form': form, 'movie': movie})


@login_required()
@own_news
def delete_news(request, movie_id):
    news = get_object_or_404(Product, id=movie_id)
    title = news.title
    news.delete()
    messages.success(request, f'A movie by name "{title}" was deleted."')
    return redirect('/news/main/')


def login_profile(request):
    if request.user.is_authenticated:
        return redirect('/')

    form = LoginForm()
    message = None

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Welcome to workspace "{user.first_name} {user.last_name}"')
                return redirect('/news/main/')
            message = f'Invalid username or password.'

    return render(request, 'auth/login.html', {'form': form, 'message': message})


def logout_profile(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')


def register(request):
    if request.user.is_authenticated:
        return redirect('/')

    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome to workspace "{user.first_name} {user.last_name}"')
            return redirect('/news/main/')

    return render(request, 'auth/register.html', {"form": form})


@login_required()
def change_profile(request):
    form = ChangeProfileForm(instance=request.user)

    if request.method == 'POST':
        form = ChangeProfileForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your profile has been updated.')
            return redirect('/news/main/')

    return render(request, 'auth/change_profile.html', {'form': form})


@login_required()
def change_password(request):
    form = ChangePasswordForm()

    if request.method == 'POST':
        form = ChangePasswordForm(data=request.POST, user=request.user)
        if form.is_valid():
            new_password = form.cleaned_data.get('new_password')
            user = request.user
            # user.password = make_password(new_password)
            user.set_password(new_password)
            user.save()

            login(request, user)

            messages.success(request, f'Your password has been changed!')
            return redirect('/news/main/')

    return render(request, 'auth/change_password.html', {'form': form})

# Create your views here.
