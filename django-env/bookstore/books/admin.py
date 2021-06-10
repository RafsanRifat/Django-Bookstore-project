from django.contrib import admin

# Register your models here.

from books.models import Book,Authors


admin.site.register(Book)
admin.site.register(Authors)
