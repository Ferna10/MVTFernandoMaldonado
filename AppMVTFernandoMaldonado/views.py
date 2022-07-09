from django.http import HttpResponse
from django.shortcuts import render
from AppMVTFernandoMaldonado.models import Padre, Madre, Hija_Mayor, Hija_Menor
import datetime
from django.template import loader

def padre(request):
    parentesco= "Padre"
    nombre="Jorge"
    apellido="Maldonado"
    edad=70
    profesion="Medico Radiologo en clinica Jesus Maria"
    fecha=datetime.datetime.now()
    nacimiento=int(fecha.year)-int(edad)

    diccionario={'fecha':fecha,'nacimiento':nacimiento,'parentesco':parentesco, 'nombre':nombre,'apellido':apellido,'edad':edad,'profesion':profesion}
    plantilla=loader.get_template('template.html')
    documento1=plantilla.render(diccionario)
    
    return HttpResponse(documento1)

def madre(request):
    parentesco="Madre"
    nombre="Araminta"
    apellido="cabrera"
    edad=60
    profesion="Perito grafologa y docente de grafologia"
    fecha=datetime.datetime.now()
    nacimiento=int(fecha.year)-int(edad)
    
    diccionario={'fecha':fecha,'nacimiento':nacimiento,'parentesco':parentesco, 'nombre':nombre,'apellido':apellido,'edad':edad,'profesion':profesion}
    plantilla=loader.get_template('template.html')
    documento1=plantilla.render(diccionario)
    
    return HttpResponse(documento1)

def hija_mayor(request):
    parentesco="Hija mayor"
    nombre="Mara"
    apellido="Maldonado"
    edad=33
    profesion="Cocinera vegana"
    fecha=datetime.datetime.now()
    nacimiento=int(fecha.year)-int(edad)

    diccionario={'fecha':fecha,'nacimiento':nacimiento,'parentesco':parentesco, 'nombre':nombre,'apellido':apellido,'edad':edad,'profesion':profesion}
    plantilla=loader.get_template('template.html')
    documento1=plantilla.render(diccionario)
    
    return HttpResponse(documento1)

def hija_menor(request):
    parentesco="Hija menor junto a mi hermano mellizo"
    nombre="Ariana"
    apellido="Maldonado"
    edad=30
    profesion="Licenciada en nutricion y tutora de academia Coderhouse"
    fecha=datetime.datetime.now()
    nacimiento=int(fecha.year)-int(edad)

    diccionario={'fecha':fecha,'nacimiento':nacimiento,'parentesco':parentesco, 'nombre':nombre,'apellido':apellido,'edad':edad,'profesion':profesion}
    plantilla=loader.get_template('template.html')
    documento1=plantilla.render(diccionario)
    
    return HttpResponse(documento1)
