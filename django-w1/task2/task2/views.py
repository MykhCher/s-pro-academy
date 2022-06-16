from django.http import HttpRequest, HttpResponse

def helloname(request, name):
    return HttpResponse(f"Hello, {name}") 