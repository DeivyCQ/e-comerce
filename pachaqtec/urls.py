from django.conf.urls import url 
from pachaqtec import views 
 
urlpatterns = [ 
    url(r'^api/tipo_imagen$', views.tipo_imagen_list),
    url(r'^api/tipo_imagen/(?P<pk>[0-9]+)$', views.tipo_imagen_detail),
    url(r'^api/tipo_imagen/published$', views.tipo_imagen_list_published)
]