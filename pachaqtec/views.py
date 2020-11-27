from rest_framework import generics
from .models import Tipo_Imagen, Producto, Imagen_Producto, Plan_Estudio, Unidad_Estudio, Sub_Unidad_Estudio
from .serializers import Tipo_Imagen_Serializer, ProductoSerializer, Imagen_ProductoSerializer, Plan_EstudioSerializer, Unidad_EstudioSerializer, Sub_Unidad_EstudioSerializer

class Tipo_Imagen_List(generics.ListCreateAPIView):
    queryset = Tipo_Imagen.objects.all()
    serializer_class = Tipo_Imagen_Serializer

class Tipo_Imagen_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tipo_Imagen.objects.all()
    serializer_class = Tipo_Imagen_Serializer

class Producto_List(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class Producto_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class Imagen_Producto_List(generics.ListCreateAPIView):
    queryset = Imagen_Producto.objects.all()
    serializer_class = Imagen_ProductoSerializer

class Imagen_Producto_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Imagen_Producto.objects.all()
    serializer_class = Imagen_ProductoSerializer

class Plan_Estudio_List(generics.ListCreateAPIView):
    queryset = Plan_Estudio.objects.all()
    serializer_class = Plan_EstudioSerializer

class Plan_Estudio_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plan_Estudio.objects.all()
    serializer_class = Plan_EstudioSerializer

class Unidad_Estudio_List(generics.ListCreateAPIView):
    queryset = Unidad_Estudio.objects.all
    serializer_class = Unidad_EstudioSerializer

class Unidad_Estudio_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Unidad_Estudio.objects.all
    serializer_class = Unidad_EstudioSerializer

class Sub_Unidad_Estudio_List(generics.ListCreateAPIView):
    queryset = Sub_Unidad_Estudio.objects.all()
    serializer_class = Sub_Unidad_EstudioSerializer

class Sub_Unidad_Estudio_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sub_Unidad_Estudio.objects.all()
    serializer_class = Sub_Unidad_EstudioSerializer