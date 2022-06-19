from django.urls import path
from .views import author_detail, book_detail, book_list, book_authlist

urlpatterns = [
    path('', book_list, name='book_list'),
    path('/book/<book_id>', book_detail, name='book_detail'),
    path('/auth/<auth_id>', author_detail, name='auth_detail'),
    path('/book/by_auth/<auth_id>', book_authlist, name='book_authlist'),
]
