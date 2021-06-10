from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now=True)



class Book(models.Model):
    title = models.CharField(max_length=256)
    pageCount = models.IntegerField(default= 0)
    thumbnailUrl = models.CharField(max_length=256, null=True)
    shortDescription = models.CharField(max_length=256, null=True)
    longDescription = models.TextField(null=True)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title


class Review(models.Model):
    body = models.TextField()
    # book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    # book_id = models.BigIntegerField(default=1)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)



