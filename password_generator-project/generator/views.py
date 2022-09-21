from calendar import c
from django.shortcuts import render
from random import *


# Create your views here.
def home(request):
    return render(request, 'generator/home.html') 

def Cruella(request):
    return render(request, 'generator/Cruella.html') 

def HarleyQuinn(request):
    return render(request, 'generator/HarleyQuinn.html') 

def password(request):
    a = list('abcdefghijklmnopqrstuvwxyz')
    password = ''

    lenght = int(request.GET.get('lenght')) 
    if request.GET.get('uppercase'):
        a.extend('abcdefghijklmnopqrstuvwxyz'.upper())
    if request.GET.get('numbers'):
        a.extend('0123456789')
    if request.GET.get('special'):
        a.extend('!@#$%^&*()_+') 

    for _ in range(lenght):
        password += choice(a)

    return render(request, 'generator/password.html', {'magic':password})


