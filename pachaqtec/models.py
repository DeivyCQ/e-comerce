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

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80)
    descripcion = models.TextField()
    descripcion_corta = models.TextField()
    descripcion_larga = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    telefono = models.CharField(max_length=20)
    orientado_a = models.CharField(max_length=255)
    otorga = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.nombre} {self.descripcion} {self.descripcion_corta} {self.descripcion_larga} {self.precio} {self.telefono} {self.orientado_a} {self.otorga}'
    
    class Meta():
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

class Imagen_Producto(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_imagen = models.ForeignKey(Tipo_Imagen, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=80)
    slug = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.tipo_imagen} {self.producto} {self.nombre} {self.slug}'

    class Meta():
        verbose_name = 'Imagen de Producto'
        verbose_name_plural = 'Imagenes del Producto'

class Plan_Estudio(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion

    class Meta():
        verbose_name = 'Plan de Estudio'
        verbose_name_plural = 'Planes de Estudio'

class Unidad_Estudio(models.Model):
    id = models.AutoField(primary_key=True)
    plan_estudio = models.ForeignKey(Plan_Estudio, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.plan_estudio} {self.descripcion}'

    class Meta():
        verbose_name = 'Unidad de Estudio'
        verbose_name_plural = 'Unidades de Estudio'
    
class Sub_Unidad_Estudio(models.Model):
    id = models.AutoField(primary_key=True)
    unidad_estudio = models.ForeignKey(Unidad_Estudio, on_delete=models.CASCADE)
    nivel = models.IntegerField(1)
    posicion = models.IntegerField()
    descripcion = models.CharField(max_length=100)
    estado = models.BooleanField()

    def __str__(self):
        return f'{self.unidad_estudio} {self.nivel} {self.posicion} {self.descripcion} {self.estado}'

    class Meta():
        verbose_name = 'Sub Unidad de Estudio'
        verbose_name_plural = 'Sub Unidades de Estudio'

