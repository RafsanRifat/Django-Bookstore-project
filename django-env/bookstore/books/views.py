from django.http import HttpResponse
from django.shortcuts import render
from books.models import Book
from django.http import Http404





# Create your views here.
def index(request):
    # return HttpResponse('Hello Books App')  eita savabik khetre. r templates er somoy return render use korte hobe, eita shortcut.
    dbData = Book.objects.all()
    context = {'books': dbData}
    return render(request, 'books/index.html', context)


def show(request, id):
    try:
        singleBook = Book.objects.get(pk=id)
    except Book.DoesNotExist:
        raise Http404("The Book you are searcing for is not exist")
    context = {'book': singleBook}
    return render(request, 'books/show.html', context)