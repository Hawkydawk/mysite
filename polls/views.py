from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hi, Hawk! You can do it well.")