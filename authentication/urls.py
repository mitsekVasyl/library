"""
    URL configuration for authentication
"""
from django.urls import path
from . import views

app_name = 'authentication'
urlpatterns = [
    # Homepage
    path('', views.index, name='index'),
    path('users/', views.get_users, name='get_users'),
    path('users/<int:user_id>/', views.user, name='user')
]