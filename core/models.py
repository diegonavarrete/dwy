from django.db import models

# Create your models here.


class insumo(models.Model):
    nombre = models.CharField(max_length=20)
    precio = models.IntegerField()
    descripcion = models.TextField()
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre


class TipoUsuario(models.Model):
    tipo = models.CharField(max_length=40)

    def __str__(self):
        return self.tipo


class Usuario(models.Model):
    rut = models.CharField(max_length=12)
    nombres = models.CharField(max_length=40)
    edad = models.IntegerField()
    tipo = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.rut

class Vision(models.Model):
    Vision = models.CharField(max_length=40)
    Mision = models.CharField(max_length=40)

    def __str__(self):
        return self.Vision

class Galeria(models.Model):
    nombre = models.CharField(max_length=40)
    imagen = models.ImageField(upload_to="insumos", null = True)

    def __str__(self):
        return self.nombre

