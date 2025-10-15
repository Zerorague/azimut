from django.contrib import admin
from inicio.models import Servicio

# Register your models here.
@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')