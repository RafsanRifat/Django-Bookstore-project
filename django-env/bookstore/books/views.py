from django.http import HttpResponse
from django.shortcuts import render
from books.models import Book





# Create your views here.
def index(request):
    # return HttpResponse('Hello Books App')  eita savabik khetre. r templates er somoy return render use korte hobe, eita shortcut.
    dbData = Book.objects.all()
    context = {'books': dbData}
    return render(request, 'books/index.html', context)


def show(request, id):
    singleBook =list()
    for book in data:
        if book['id'] == id:
            singleBook = book
    context = {'book': singleBook}
    return render(request, 'books/show.html', context)