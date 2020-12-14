from django.urls import path
from . import views

app_name = 'book'
urlpatterns = [
    # Books page
    path('books/', views.books, name='books'),
    path('books/<int:book_id>', views.book, name='book')
]