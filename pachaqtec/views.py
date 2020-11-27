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
        producto = queryset.values()
        prod = []
        for p in producto:
            # Imágenes de curso.
            img_principal = ""
            img_slider = ""
            imagen_producto = Imagen_Producto.objects.filter(producto=p["id"])
            for ip in imagen_producto.values():
                print(ip)
                if ip["tipo_imagen_id"] == 1:
                    img_principal = ip["nombre"]
                if ip["tipo_imagen_id"] == 2:
                    img_slider= ip["nombre"]
            # Plan de estudio.
            plan_estudio = Plan_Estudio_Producto.objects.filter(producto_id=p["id"])

            p["descripcion_corta"].replace("\r", "")

            # JSON Estructura
            prod.append({
                "id" : p["id"],
                "nombre" : p["nombre"],
                "img" : img_principal,
                "precio" : p["precio"],
                "descuento": 20,
                "imgSlider" : img_slider,
                "frase" : p["descripcion"],
                "descripcion" : p["descripcion_corta"],
                "inicioClases" : p["inicio_clases"],
                "horario" : [
                    {
                        "frecuencia": "Lunes, martes, miércoles",
                        "hora": "7:30 p.m a 9:30 p.m"
                    },
                    {
                        "frecuencia": "Jueves (asesoría)",
                        "hora": "7:30 p.m a 9:30 p.m"
                    },
                    {
                        "frecuencia": "Sábados",
                        "hora": "8:00 a.m a 2:00 p.m"
                    }
                ],
                "planEstudio" : [
                    {
                        "titulo": "",
                        "semanas": [
                            {
                                "titulo" : "",
                                "Subtemas": ["",""]
                            }
                        ]
                    }
                ]
                #"descripcion_corta" : p["descripcion_corta"],
                #"descripcion_larga" : p["descripcion_larga"],
                #"telefono" : p["telefono"],
                #"orientado_a" : p["orientado_a"],
                #"otorga" : p["otorga"]
                })
        
        # print(prod)
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