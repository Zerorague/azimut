from django.contrib import admin
from inicio.models import Servicio, Cotizacion

# Register your models here.
@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')

@admin.register(Cotizacion)
class CotizacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'servicio', 'mensaje', 'fecha_solicitud')
    list_filter = ('servicio', 'fecha_solicitud')
    search_fields = ('nombre', 'email', 'telefono')
    date_hierarchy = 'fecha_solicitud'
