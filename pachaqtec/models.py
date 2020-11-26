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