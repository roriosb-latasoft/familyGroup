from django.db import models

# Create your models here.from django.db import models

class Corredor(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)  # RUT único
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(unique=True)
    imagen = models.ImageField(upload_to='img/fotosCorredores/', blank=True, null=True)
    

    def __str__(self):
        return self.nombre


class Propiedad(models.Model):
    # Otras campos ya existentes en el modelo
    nombre = models.CharField(max_length=200)
    valor_clp = models.DecimalField(max_digits=12, decimal_places=2)
    direccion = models.CharField(max_length=300)
    habitaciones = models.IntegerField()
    metros_cuadrados = models.DecimalField(max_digits=10, decimal_places=2)
    banos = models.IntegerField()
    imagen = models.ImageField(upload_to='img/fotoCasas/')
    
    # Campo para definir si es para venta o arriendo
    TIPO_PROP = [
        ('venta', 'Venta'),
        ('arriendo', 'Arriendo'),
    ]
    
    tipo = models.CharField(max_length=10, choices=TIPO_PROP, default='venta')

    # Corredor (como mencionabas en el modelo anterior)
    corredor = models.ForeignKey('Corredor', on_delete=models.CASCADE)