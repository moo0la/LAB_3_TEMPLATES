from django.shortcuts import render

import datetime

from django.http import HttpRequest, HttpResponse

def today(request : HttpRequest):
    t = datetime.date.today()
    return render(request, 'today/index.html', {"today": t})