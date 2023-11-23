from django.contrib import admin
from .models import Ciudad
# Register your models here.
class CiudadAdmin(admin.ModelAdmin):
    list_display = ["nombre","descripcion","año","dias","calificacion"]

admin.site.register(Ciudad,CiudadAdmin)