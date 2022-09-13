import random
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def randompass(request):

    characters = list('!@#$%&_0987654321abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    randompass = ''
    for x in range(10):
        randompass += random.choice(characters)
    return render(request, 'randompass/index.html', {'pass':randompass}) 