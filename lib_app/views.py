from django.shortcuts import render

from .models import Book 

from django.http import HttpResponse
# Create your views here.
def home(request):
    books = Book.objects.all()
    return render(request, 'lib_app/home.html', {'books': books})

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'lib_app/book_detail.html', {'book': book})
