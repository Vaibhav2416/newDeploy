from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("This is Home")

def new(request):
    return HttpResponse("Updating Response here")