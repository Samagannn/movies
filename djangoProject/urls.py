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

from movies.urls import urlpatterns as movies_urls
from workspace.urls import urlpatterns as workspace_urls
from workspace import views as workspace_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include(movies_urls)),
    path('auth/login/', workspace_views.login_profile, name='login'),
    path('auth/logout/', workspace_views.logout_profile, name='logout'),
    path('auth/register/', workspace_views.register, name='register'),
    path('auth/change_profile', workspace_views.change_profile, name='change_profile'),
    path('auth/change_password/', workspace_views.change_password, name='change_password'),
    path('', lambda r: redirect('/news/'), name='main'),
    path('news/', include(workspace_urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
