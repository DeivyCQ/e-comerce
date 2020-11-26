from rest_framework import serializers
from pachaqtec.models import Tipo_Imagen, Imagen_Producto, Producto, Unidad_Estudio, Plan_Estudio, Sub_Unidad_Estudio


class Tipo_Imagen_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tipo_Imagen
        fields = ('id',
        'descripcion')

class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        pass

class Imagen_ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        pass

class Plan_EstudioSerializer(serializers.ModelSerializer):

    class Meta:
        pass

class Unidad_EstudioSerializer(serializers.ModelSerializer):

    class Meta:
        pass

class Sub_Unidad_EstudioSerializer(serializers.ModelSerializer):

    class Meta:
        pass