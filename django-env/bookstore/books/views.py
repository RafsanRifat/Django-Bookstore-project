from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    # return HttpResponse('Hello Books App')  eita savabik khetre. r templates er somoy return render use korte hobe, eita shortcut.
    return render(request, 'index.html', )
