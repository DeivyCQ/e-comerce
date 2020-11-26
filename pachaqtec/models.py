from django.db import models

# Create your models here.

class Tipo_Imagen(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=20)

    def __str__(self):
        return self.descripcion
    
    class Meta():
        verbose_name = 'Tipo Imagen'
        verbose_name_plural = 'Tipos de Imagen'

class Imagen_Producto(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_imagen = models.ForeignKey(Tipo_Imagen on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto on_delete=models.CASCADE)
    nombre = models.CharField(max_length=80)
    slug = models.CharField(max_length=255)
    
class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80)
    descripcion = models.TextField
    descripcion_corta = models.TextField()
    descripcion_larga = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    telefono = models.CharField(max_length=20)
    orientado_a = models.CharField(max_length=255)
    otorga = models.CharField(max_length=255)

class Plan_Estudio(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)

class Unidad_Estudio(models.Model):
    id = models.AutoField(primary_key=True)
    plan_estudio = models.ForeignKey(Plan_Estudio on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100)
    

class Sub_Unidad_Estudio(models.Model):
    id = models.AutoField(primary_key=True)
    