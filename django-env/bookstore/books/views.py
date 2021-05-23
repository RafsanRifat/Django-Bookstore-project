from django.http import HttpResponse
from django.shortcuts import render
import json
from pathlib import Path

booksData = open("books.json").read()
data = json.loads(booksData)



# Create your views here.
def index(request):
    # return HttpResponse('Hello Books App')  eita savabik khetre. r templates er somoy return render use korte hobe, eita shortcut.
    context = {'books': data}
    return render(request, 'books/index.html', context)
