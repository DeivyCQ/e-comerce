from django.contrib import admin
from .models import Tipo_Imagen, Producto, Imagen_Producto, Plan_Estudio, Plan_Estudio_Producto, Unidad_Estudio, Sub_Unidad_Estudio

# Register your models here.
admin.site.register(Tipo_Imagen)
admin.site.register(Producto)
admin.site.register(Imagen_Producto)
admin.site.register(Plan_Estudio)
admin.site.register(Unidad_Estudio)
admin.site.register(Sub_Unidad_Estudio)
admin.site.register(Plan_Estudio_Producto)