from django.db import models
from django.core.validators import MinValueValidator

class Vehiculo(models.Model):
    
    FORD = "Ford"
    CHEVROLET = "Chevrolet"
    FIAT = "Fiat"
    TOYOTA = "Toyota"
    MARCA_CHOICES = [
        (FORD, "Ford"),
        (CHEVROLET, "Chevrolet"),
        (FIAT, "Fiat"),
        (TOYOTA, "Toyota")
    ]

    PARTICULAR = "Particular"
    TRANSPORTE = "Transporte"
    CARGA = "Carga"
    CATEGORIA_CHOICES = [
        (PARTICULAR, "Particular"),
        (TRANSPORTE, "Transporte"),
        (CARGA, "Carga"),
    ]

    marca = models.CharField(max_length=20, choices=MARCA_CHOICES, default=FORD)
    modelo = models.CharField(max_length=100, null=False)
    serial_carroceria = models.CharField(max_length=50, null=False)
    serial_motor = models.CharField(max_length=50, null=False)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, default=PARTICULAR)
    precio = models.IntegerField(validators=[MinValueValidator(limit_value=0)])
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)
    fecha_de_modificacion = models.DateTimeField(auto_now=True)
