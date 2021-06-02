from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from books.models import Book, Review
from django.http import Http404






# Create your views here.
def index(request):
    # return HttpResponse('Hello Books App')  eita savabik khetre. r templates er somoy return render use korte hobe, eita shortcut.
    dbData = Book.objects.all()
    context = {'books': dbData}
    return render(request, 'books/index.html', context)


def show(request, id):
    """    try:
           singleBook = Book.objects.get(pk=id)
       except Book.DoesNotExist:
           raise Http404("The Book you are searcing for is not exist")
       context = {'book': singleBook}
       return render(request, 'books/show.html', context)
    """
    singleBook = get_object_or_404(Book, pk=id)  # we can use this shortcut if we don't want to use the above method
    reviews = Review.objects.all()
    context = {'book' : singleBook, 'reviews': reviews}
    return render(request, 'books/show.html', context)

def reviews(request, id):
    book = get_object_or_404(Book, id=id)
    body = request.POST['review']

    newReview = Review(body=body, book=book)
    newReview.save()

    return redirect('/books/{book_id}'.format(book_id=id))
