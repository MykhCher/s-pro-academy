from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponseNotFound
from .models import Author, Books
from .forms import CreateBook

def book_list(request):
    bookz = Books.objects.all()
    if "search" in request.GET:
        search=request.GET['search']
        bookz=Books.objects.filter(title__icontains=search)
    if request.method=='POST':
        form=CreateBook(request.POST)
        if form.is_valid:
            form.save()
            bookz = Books.objects.all()
    context={'books':bookz, 'book_form':CreateBook}
    return render(request, 'book_list.html', context=context)

def book_detail(request, book_id):
    book = Books.objects.get(pk=int(book_id))
    return render(request, "book_details.html", context = {'book':book})


def author_detail(request, auth_id):
    auth = get_object_or_404(Author, pk=int(auth_id))
    return render(request, "auth_details.html", context = {'author':auth})

def book_authlist(request, auth_id):
    books = list()
    for i in Books.objects.all():
        if i.author.pk == auth_id:
            books.append(i)
    return render(request, 'books_authlist.html', context={'books' : books})
    