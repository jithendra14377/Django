from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse('Welcome to Django Training')

def add(request,x,y):
    return HttpResponse(f'The sum of {x} and {y} is {x+y}')

def add2(request):
    x=int(request.GET['x'])
    y=int(request.GET['y'])
    c=x+y
    return HttpResponse(f'The sum of {x} and {y} is {c}')