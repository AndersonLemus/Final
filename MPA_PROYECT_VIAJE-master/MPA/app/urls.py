from django.contrib import admin
from django.urls import path
from .views import home,agregar_ciudad,listar_ciudades,modificar_ciudad, \
    eliminar_ciudad, registro
urlpatterns = [
    path('',home,name="home"),
    path('agregar-ciudad/',agregar_ciudad,name="agregar_ciudad"),
    path('listar-ciudades/',listar_ciudades,name="listar_ciudades"),
    path('modificar-ciudad/<id>/',modificar_ciudad,name="modificar_ciudad"),
    path('eliminar-ciudad/<id>/',eliminar_ciudad,name="eliminar_ciudad"),
    path('registro/', registro, name="registro"),
    

]
