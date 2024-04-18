from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('u/<str:username>/', views.user_links_page, name='user_links_page'),
    path('contact/', views.contact, name='contact'),
    path('terms/', views.terms, name='terms')
]