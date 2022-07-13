from django import forms
from .models import Books

class CreateBook(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'released_year', 'description', 'author']
