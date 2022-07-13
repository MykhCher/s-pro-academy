from pydoc import describe
from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()

    @staticmethod
    def author_create():
        for i in authors:
            author = Author(
                first_name=i['first_name'],
                last_name=i['last_name'],
                age=i['age']
            )
            author.save()

class Books(models.Model):
    title = models.CharField(max_length=100)
    released_year = models.IntegerField()
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def book_save():
        for i in books:
            author_id = Author.objects.get(pk=i['author'])
            book = Books(
                title=i['title'],
                released_year=i['released_year'],
                description=i['description'],
                author = author_id
            )
            book.save()

