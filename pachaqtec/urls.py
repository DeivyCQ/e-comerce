from django.urls import path
from pachaqtec import views 
from rest_framework.urlpatterns import format_suffix_patterns
 
urlpatterns = [ 
    #tipo_imagen
    path('imagen/', views.Tipo_Imagen_List.as_view()),
    path('imagen-<int:pk>/', views.Tipo_Imagen_Detail.as_view()),
    #producto
    path('producto/', views.Producto_List.as_view()),
    path('producto-<int:pk>/', views.Producto_Detail.as_view()),
    #imagen_producto
    path('imagenproducto/', views.Imagen_Producto_List.as_view()),
    path('imagenproducto-<int:pk>/', views.Imagen_Producto_Detail.as_view()),
    #plan_estudio
    path('planestudio/', views.Plan_Estudio_List.as_view()),
    path('planestudio-<int:pk>/', views.Plan_Estudio_Detail.as_view()),
    #unidad_estudio
    path('unidad/', views.Unidad_Estudio_List.as_view()),
    path('unidad-<int:pk>/', views.Unidad_Estudio_Detail.as_view()),
    #subunidad_estudio
    path('subunidad/', views.Sub_Unidad_Estudio_List.as_view()),
    path('subunidad-<int:pk>/', views.Sub_Unidad_Estudio_Detail.as_view()),
]

#urlpatterns = format_suffix_patterns(urlpatterns)