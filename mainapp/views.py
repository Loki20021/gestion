from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello (request):
    return HttpResponse('<h1> HELLO World</h1>')

def page_accueil(request):
    return render( request, 'mainapp/page_acceuil.html')
