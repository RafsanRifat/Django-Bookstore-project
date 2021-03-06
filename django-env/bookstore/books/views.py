from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from books.models import Book, Review
from django.http import Http404
from django.views.generic import ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin






# Create your views here.
"""def index(request):
    # return HttpResponse('Hello Books App')  eita savabik khetre. r templates er somoy return render use korte hobe, eita shortcut.
    dbData = Book.objects.all()
    context = {'books': dbData}
    return render(request, 'books/book_list.html', context)"""

# we can do this like bellow ----->>>

class BookListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return Book.objects.all()


# def show(request, id):
    """    try:
           singleBook = Book.objects.get(pk=id)
       except Book.DoesNotExist:
           raise Http404("The Book you are searcing for is not exist")
       context = {'book': singleBook}
       return render(request, 'books/book_detail.html', context)
    """
"""    singleBook = get_object_or_404(Book, pk=id)  # we can use this shortcut if we don't want to use the above method
    reviews = Review.objects.filter(book_id=id).order_by('-created_at')
    context = {'book' : singleBook, 'reviews': reviews}
    return render(request, 'books/book_detail.html', context)"""
# we CAN DO this like below:

class BookDetailView(LoginRequiredMixin,DetailView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = context['book'].review_set.order_by('-created_at')
        context['authors'] = context['book'].authors.all()
        return context


def author(request, author):
    books = Book.objects.filter(authors__name=author)
    context = {'book_list': books}
    return render(request, 'books/book_list.html', context)


def reviews(request, id):
    # book = get_object_or_404(Book, id=id)
    body = request.POST['review']
    newReview = Review(body=body, book_id= id)
    newReview.save()
    return redirect('/books')
