from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello world")

def hello_name(request, name):
    return HttpResponse(f"Hello <h1> {name} </h1> !")

def your_age(request, age):
    return HttpResponse(f"you are <h1>{age}</h1> year old")