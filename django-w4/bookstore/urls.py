from django.urls import path
from .views import author_detail, book_detail, book_list, book_authlist, book_creation

urlpatterns = [
    path('', book_list, name='book_list'),
    path('book/<int:book_id>', book_detail, name='book_detail'),
    path('auth/<int:auth_id>', author_detail, name='auth_detail'),
    path('book/by_auth/<int:auth_id>', book_authlist, name='book_authlist'),
    path('book_creation', book_creation, name='book_creation')
]
