from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name= 'book.all'),  # eikhane /book path a jokhon kono request ashbe, tokhon eita views file er index function
                            # k load korbe, r tarpor response korbe.   # static rout er khetre path eivabe likha hoise.
                            # prothome empty '' er ortho main path bujhay
    path('<int:id>', views.show, name= 'book.show'),   # Dynamic rout er khetre path define kora hoy eivabe...
                                                # 3rd argument hisebe name use kora jay. name hisebe jekono kichu, jekono
                                                # formatei use kora jay. eikhane emnitei book.show eivabe use koresi.
                                                # "book-show, show_page, pageShow.  eirokom jekono vabei use kora jeto"
    path('review', views.review, name='book.review')

]
