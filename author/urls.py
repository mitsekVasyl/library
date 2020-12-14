from django.urls import path
from . import views

app_name = 'author'
urlpatterns = [
    path('authors/', views.authors, name='authors'),
    path('authors/<int:author_id>/', views.author, name='author'),
    path('authors/books/<int:author_id>/', views.author_books, name='author_books')
]