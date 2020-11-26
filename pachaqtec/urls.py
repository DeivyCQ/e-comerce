from django.urls import path
from pachaqtec import views 
 
urlpatterns = [ 
    path('imagen/', views.Tipo_Imagen_List.as_view()),
    path('imagen/<int:pk>/', views.Tipo_Imagen_Detail.as_view()),
]