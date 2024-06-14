"""
URL configuration for fmartns project.

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
from django.contrib import admin
from django.urls import path, include
from accounts import views
from django.contrib.auth.views import logout_then_login
from django.views.generic import TemplateView
from django.urls import re_path
from django.views.static import serve
from django.conf import settings

handler404 = 'main.views.page_not_found'

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_then_login, name='logout'),
    path('accounts/register/', views.register, name='register'),
    path('dashboard/', include('dashboard.urls')),
    path('helloworld/', TemplateView.as_view(template_name="helloworld.html"), name='helloworld'),
    path('vacation/', TemplateView.as_view(template_name="vacation.html"), name='vacation'),
    path('silvia/', TemplateView.as_view(template_name="silvia.html"), name='vacation'),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]