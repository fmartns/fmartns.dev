from django.urls import path
from . import views
from django.contrib.auth.views import PasswordChangeView
from .views import CustomPasswordChangeView


urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("administration/", views.administration, name="administration"),
    path('administration/links/', views.social_media_list, name='social_media_list'),
    path('toggle-active/', views.toggle_active, name='toggle_active'),
    path('delete-link/', views.delete_link, name='delete_link'),
    path('reorder-links', views.reorder_links, name='reorder_links'),
    path('administration/links/add/', views.social_media_add, name='social_media_add'),
    path('administration/links/<int:pk>/delete/', views.social_media_delete, name='social_media_delete'),
    path('links/', views.manage_social_media, name='manage_social_media'),
    path('profile/delete/<int:pk>/', views.user_social_media_delete, name='user_social_media_delete'),
    path('profile', views.manage_preferences, name='manage_preferences'),
    path('profile/change-password/', CustomPasswordChangeView.as_view(template_name='dashboard/change_password.html'), name='change_password'),
]