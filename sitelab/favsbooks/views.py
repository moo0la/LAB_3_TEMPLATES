from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
def book(request : HttpRequest):
    book = ["introduction to CS ", "FinTech", "Python for bigner "]
    return render(request, 'favsbooks/index.html', { "book" : book})
