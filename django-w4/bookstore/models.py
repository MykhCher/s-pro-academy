from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    
    def __str__(self):
        return f'{self.pk}. {self.first_name} {self.last_name}'

class Books(models.Model):
    title = models.CharField(max_length=100)
    released_year = models.IntegerField()
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class Review(models.Model):
    book = models.ForeignKey(Books, related_name="reviews", on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField() 
