from django.shortcuts import render, get_object_or_404
from .models import Book

def books(request):
    books = Book.objects.all().order_by('id')
    context = {'books': books}
    return render(request, 'book/books.html', context)

def book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    context = {'book': book}
    return render(request, 'book/book.html', context)