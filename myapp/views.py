from django.shortcuts import render
from django.http import HttpResponse

def saludo(request): 
    return HttpResponse("Hola Django - Coder")

def index(request):
    context = {"mensaje": "Bienvenidos a mi aplicacion Django"}
    return render(request, "myapp/index.html", context)