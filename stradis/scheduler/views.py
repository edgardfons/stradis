from django.shortcuts import render
from . import resolver
from django import forms
from faker import Faker
from scheduler.models import *

def index(request):
    return render(request, 'scheduler/index.html')

def schedule(request): 

    context = {}
    teachers = []
    fake = Faker()

    for i in range(10):
        teachers.append( Teacher(i, fake.name()) )

    print(teachers)

    resolver.egMyModel()

    return render(request, 'scheduler/index.html', context)