from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def hellodjango(request : HttpRequest):
    return HttpResponse('Hello Django!')