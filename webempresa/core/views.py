from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("Hola")

def about(request):
    return HttpResponse("Hola")

def services(request):
    return HttpResponse("Hola")

def store(request):
    return HttpResponse("Hola")

def contact(request):
    return HttpResponse("Hola")

def blog(request):
    return HttpResponse("Hola")

def sample(request):
    return HttpResponse("Hola")
