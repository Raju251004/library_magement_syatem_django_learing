from django.shortcuts import render

from .models import Book 

from django.http import HttpResponse
# Create your views here.

def home(request): #requst for the home page
    books = Book.objects.all()
    search_query = request.GET.get("search",' ')
    category = request.GET.get("category",' ') #category filter dropdown
    if search_query:   #
        books = books.filter(title__icontains=search_query)

    if category:  #category filter dropdown
        books = books.filter(category=category)
        categories = Book.objects.values_list('category', flat=True).distinct()
    return render(request, 'lib_app/home.html', {'books': books, 'categories': categories,})

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'lib_app/book_detail.html', {'book': book})
# def test(request):
#     categories = Book.objects.values_list('category', flat=True).distinct()
#     return render(request, 'lib_app/test.html', {'categories': categories})

def test(request):
    books = Book.objects.all()
    return render(request, 'lib_app/test.html', {'books': books})