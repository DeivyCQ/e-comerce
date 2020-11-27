from rest_framework import generics
from .models import Tipo_Imagen, Producto, Imagen_Producto, Plan_Estudio, Unidad_Estudio, Sub_Unidad_Estudio, Plan_Estudio_Producto
from .serializers import Tipo_Imagen_Serializer, ProductoSerializer, Imagen_ProductoSerializer, Plan_EstudioSerializer, Unidad_EstudioSerializer, Sub_Unidad_EstudioSerializer
from rest_framework.response import Response
from django.core import serializers

class Tipo_Imagen_List(generics.ListCreateAPIView):
    queryset = Tipo_Imagen.objects.all()
    serializer_class = Tipo_Imagen_Serializer

class Tipo_Imagen_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tipo_Imagen.objects.all()
    serializer_class = Tipo_Imagen_Serializer

class Producto_List(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def list(self, request):
        queryset = self.get_queryset()
        # producto = serializers.serialize("json", queryset)
        producto = queryset.values()
        print(queryset.values())
        prod = []
        for p in producto:
            # print(p["nombre"])
            imagen_producto = Imagen_Producto.objects.filter(producto=p["id"])
            plan_estudio = Plan_Estudio_Producto.objects.filter(producto_id=p["id"])
            print(imagen_producto.values()) 
            print(plan_estudio.values())
            prod.append({
                "nombre" : p["nombre"],
                "alumno" : "nombrealumno",
                "imagen" : imagen_producto.values(),
                "planEstudio" : plan_estudio.values()
            })
        
        print(prod)
        serializer = ProductoSerializer(queryset, many=True)
        return Response(prod)

class Producto_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    lookup_field = "slug"


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