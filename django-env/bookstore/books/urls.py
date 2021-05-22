from . import views
from django.urls import path

urlpatterns = [
    path('', views.index)  # eikhane /book path a jokhon kono request ashbe, tokhon eita views file er index function
                                # k load korbe, r tarpor response korbe


]