from django.shortcuts import render, get_object_or_404

from .models import Author
from book.models import Book

def authors(request):
    authors = Author.objects.all().order_by('id')
    context = {'authors': authors}
    return render(request, 'author/authors.html', context)

def author(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    context = {'author': author}
    return render(request, 'author/author.html', context)

def author_books(request, author_id):
    books = Book.objects.filter(authors=author_id).order_by('id')
    context = {'books': books}
    return render(request, 'author/books.html', context)