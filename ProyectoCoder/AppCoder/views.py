from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader
from AppCoder.models import Profesor

def crear_profesor(request):
    template = loader.get_template("template1.html")
    
    profe1 = Profesor(nombre="Ricardo", apellido="Ruben", email="ricky@coder.com", profesion="abogado")
    profe2 = Profesor(nombre="Gerardo", apellido="Rasiel", email="gera@coder.com", profesion="abogado")
    profe3 = Profesor(nombre="Armando", apellido="Onel", email="arma@coder.com", profesion="contador")

    dic_de_contexto = {
        "profe_1": profe1.nombre,
        "profe_2": profe2.nombre,
        "profe_3": profe3.nombre,
    }
    res = template.render(dic_de_contexto)
    
    return HttpResponse (res)