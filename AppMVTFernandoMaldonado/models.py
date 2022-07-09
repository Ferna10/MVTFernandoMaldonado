from django.db import models

# Create your models here.
class Padre(models.Model):
    parentesco=models.CharField(max_length=50)
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    edad=models.IntegerField()
    profesion=models.CharField(max_length=30)
    fecha=models.DateTimeField()
    nacimiento=models.DateTimeField()

class Madre(models.Model):
    parentesco=models.CharField(max_length=50)
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    edad=models.IntegerField()
    profesion=models.CharField(max_length=30)
    fecha=models.DateTimeField()
    nacimiento=models.DateTimeField()

class Hija_Mayor(models.Model):
    parentesco=models.CharField(max_length=50)
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    edad=models.IntegerField()
    profesion=models.CharField(max_length=30)
    fecha=models.DateTimeField()
    nacimiento=models.DateTimeField()

class Hija_Menor(models.Model):
    parentesco=models.CharField(max_length=50)
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    edad=models.IntegerField()
    profesion=models.CharField(max_length=30)
    fecha=models.DateTimeField()
    nacimiento=models.DateTimeField()
    

