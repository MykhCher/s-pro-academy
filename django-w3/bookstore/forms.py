from django import forms
from .models import Author, Books

class CreateBook(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'released_year', 'description', 'author']

