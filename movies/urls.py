from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('<int:movie_id>', views.detail_news, name="detail_news"),
    path('news/category/<int:id>/', views.news_by_category, name='news_by_category'),
]
