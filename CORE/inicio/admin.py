from django.contrib import admin
from inicio.models import Servicio, Cotizacion, Contacto

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

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'asunto', 'mensaje', 'fecha_contacto')
    list_filter = ('fecha_contacto',)
    search_fields = ('nombre', 'email', 'telefono')
    date_hierarchy = 'fecha_contacto'
    ordering = ('-fecha_contacto',)