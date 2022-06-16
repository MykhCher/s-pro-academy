import imp
from django.http import HttpResponse
from django.urls import URLPattern


from django.urls import path
from firstapp.views import hellodjango

urlpatterns = [
    path('', hellodjango)
]