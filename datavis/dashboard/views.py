from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

dt2 = [
        1,
        2,
        3,
        8,
        5,
        6,
        7,
        ]

def index(request):
    return render (request, 'index.html', {'dt2': dt2})