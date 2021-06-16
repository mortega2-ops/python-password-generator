from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    return render(request, 'generator/home.html', {'password': 'a;dfhasdiof8i9owj'})


def password(request):
    characters = list('abcdefghigklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUV'))
    if request.GET.get('special'):
        characters.extend('!@#$%^&*()?')
    if request.GET.get('numbers'):
        characters.extend('1234567890')

    length = int(request.GET.get('length', 12))

    the_password = ''
    for x in range(length):
        the_password += random.choice(characters)

    return render(request, "generator/password.html", {'password': the_password})


def about(request):
    return render(request, "generator/about.html")




