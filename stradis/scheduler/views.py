from django.shortcuts import render
from . import resolver

def index(request):
    objeto = { 'nome': 'Edgard Oliveira' }
    return render(request, 'scheduler/index.html', { 'objeto': objeto })

def schedule(request): 
    resolver.simpleLP()   
    return render(request, 'scheduler/index.html')