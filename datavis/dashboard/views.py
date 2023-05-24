from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Cadastro
# Create your views here.

dt2 = Cadastro.objects.all()




def index(request):
    dt = []
    nm = []
    values = Cadastro.objects.all()
    for v in values:
        dt.append(v.valor)
        nm.append(v.nome)

    return render (request, 'index.html', {'dt2': dt, 'nm2' : nm})





