from rest_framework import serializers
from pachaqtec.models import Tipo_Imagen


class Tipo_Imagen_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tipo_Imagen
        fields = ('id',
        'descripcion')