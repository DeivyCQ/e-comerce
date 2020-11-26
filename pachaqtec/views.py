from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from pachaqtec.models import Tipo_Imagen
from pachaqtec.serializers import Tipo_Imagen_Serializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def tipo_imagen_list(request):
    if request.method == 'GET':
        tipos_imagen = Tipo_Imagen.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            tipos_imagen = tipos_imagen.filter(title__icontains=title)
        
        tipos_imagen_serializer = Tipo_Imagen_Serializer(tipos_imagen, many=True)
        return JsonResponse(tipos_imagen_serializer.data, safe=False)
    elif request.method == 'POST':
        tipo_imagen_data = JSONParser().parse(request)
        tipo_imagen_serializer = Tipo_Imagen_Serializer(data=tipo_imagen_data)
        if tipo_imagen_serializer.is_valid():
            tipo_imagen_serializer.save()
            return JsonResponse(tipo_imagen_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tipo_imagen_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Tipo_Imagen.objects.all().delete()
        return JsonResponse({'message': '{} Los Tipos de Imagen han Sido Eliminadas con Éxito!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def tipo_imagen_detail(request, pk):
    try: 
        tipo_imagen = Tipo_Imagen.objects.get(pk=pk) 
    except Tipo_Imagen.DoesNotExist: 
        return JsonResponse({'message': 'el tipo de imagen no existe'}, status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET': 
        tipo_imagen_serializer = Tipo_Imagen_Serializer(tipo_imagen) 
        return JsonResponse(tipo_imagen_serializer.data)
    elif request.method == 'PUT': 
        tipo_imagen_data = JSONParser().parse(request) 
        tipo_imagen_serializer = Tipo_Imagen_Serializer(tipo_imagen, data=tipo_imagen_data) 
        if tipo_imagen_serializer.is_valid(): 
            tipo_imagen_serializer.save() 
            return JsonResponse(tipo_imagen_serializer.data) 
        return JsonResponse(tipo_imagen_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE': 
        tipo_imagen.delete() 
        return JsonResponse({'message': 'El Tipo de Imagen ha sido Eliminado con Éxito!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def tipo_imagen_list_published(request):
    tipos_imagen = Tipo_Imagen.objects.filter(published=True)
        
    if request.method == 'GET': 
        tipo_imagen_serializer = Tipo_Imagen_Serializer(tipos_imagen, many=True)
        return JsonResponse(tipos_imagen_serializer.data, safe=False)