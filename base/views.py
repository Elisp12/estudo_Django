from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home (request):
    return HttpResponse('Home 2') 

def sobre(request):
    return HttpResponse('sobre')

def contato(request):
    return HttpResponse('Contato')
