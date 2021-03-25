from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('hello welcome to my home page')