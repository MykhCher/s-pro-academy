from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

def telldate(request):
    return HttpResponse(date.today())

def tellyear(request):
    return HttpResponse(date.today().year)

def tellmonth(request):
    return HttpResponse(date.today().month)
    
def tellday(request):
    return HttpResponse(date.today().day)

