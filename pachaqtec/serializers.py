from rest_framework import serializers
from pachaqtec.models import Tipo_Imagen, Imagen_Producto, Producto, Unidad_Estudio, Plan_Estudio, Sub_Unidad_Estudio


class Tipo_Imagen_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tipo_Imagen
        fields = ('id',
        'descripcion')

class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = ('id',
        'nombre',
        'descripcion',
        'descripcion_corta',
        'descripcion_larga',
        'precio',
        'telefono',
        'orientado_a',
        'otorga')

class Imagen_ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Imagen_Producto
        fields = ('id',
        'tipo_imagen',
        'producto',
        'nombre',
        'slug')

class Plan_EstudioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plan_Estudio
        fields = ('id',
        'descripcion')

class Unidad_EstudioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Unidad_Estudio
        fields = ('id',
        'plan_estudio',
        'descripcion')

class Sub_Unidad_EstudioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sub_Unidad_Estudio
        fields = ('id',
        'unidad_estudio',
        'nivel',
        'posicion',
        'descripcion',
        'estado')