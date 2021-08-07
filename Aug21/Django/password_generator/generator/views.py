from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
def home(request):
    """
    This is the home page request
    """
    return render(request, 'generator/home.html')


def about(request):
    return render(request, 'generator/about.html')


def password(request):
    generated_password = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    # Get the length from query string
    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('*&%#@'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    for index in range(length):
        generated_password += random.choice(characters)
    return render(request, 'generator/password.html', {'password': generated_password})
