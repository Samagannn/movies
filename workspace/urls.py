from django.urls import path
from . import views

urlpatterns = [
    path('', views.workspace, name='workspace'),
    path('main/', views.workspace),
    path('main/<int:movie_id>/update/', views.update_movies, name='update_movies'),
    path('main/<int:movie_id>/delete/', views.delete_news, name='delete_news'),
    path('main/create/', views.create_movies, name='create_movies'),
]
