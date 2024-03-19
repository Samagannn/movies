"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

from movies.views import main, detail_news, item_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('movies.urls')),
    path('', main, name="main"),
    path('<int:movie_id>', detail_news, name="movie_list"),
    path('<int:movie_id>', item_detail, name='item_detail'),
    path('', lambda r: redirect('/news/'), name='main')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', main, name='name'),
#     path('news/<int:id>/', detail_news, name='detail_news'),
#     path('home/', home, name='home'),
#     path('news/', include('news.urls')),
#     path('', lambda r: redirect('/news/'), name='main')
#
# ]
