from rest_framework import generics
from .models import Tipo_Imagen
from .serializers import Tipo_Imagen_Serializer

class Tipo_Imagen_List(generics.ListCreateAPIView):
    queryset = Tipo_Imagen.objects.all()
    serializer_class = Tipo_Imagen_Serializer

class Tipo_Imagen_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tipo_Imagen.objects.all()
    serializer_class = Tipo_Imagen_Serializer