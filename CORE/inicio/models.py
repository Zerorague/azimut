from django.db import models
from django_resized import ResizedImageField
from django.core.validators import RegexValidator

# Create your models here.
def nombre_imagen(instance, filename):
    # El nombre de la imagen será el nombre del servicio con la extensión original
    extension = filename.split('.')[-1]
    return f'servicios/{instance.nombre}.{extension}'

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = ResizedImageField(size=[1350, 900], upload_to= nombre_imagen, blank=True, null=True)

    def __str__(self):
        return self.nombre.capitalize()
    





class Cotizacion(models.Model):
    nombre = models.CharField(max_length=100, help_text="Nombre completo del solicitante",verbose_name="Nombre")
    region = models.CharField(max_length=100, help_text="Región del solicitante",verbose_name="Región",blank=True, null=True)
    comuna = models.CharField(max_length=100, help_text="Comuna del solicitante",verbose_name="Comuna",blank=True, null=True)
    email = models.EmailField(help_text="Correo electrónico del solicitante",verbose_name="Correo Electrónico")
    telefono = models.CharField(max_length=20, help_text="Número de teléfono del solicitante",verbose_name="Teléfono",
        validators=[RegexValidator(regex=r'^(\+56)?\d{9}$', message="El número de teléfono debe tener entre 9 y 15 dígitos y puede incluir el código de país.")])
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, help_text="Servicio para el cual se solicita la cotización",verbose_name="Servicio")
    mensaje = models.TextField(blank=True, null=True , help_text="Mensaje adicional del solicitante",verbose_name="Mensaje")
    fecha_solicitud = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Cotización de {self.nombre} para {self.servicio.nombre}'
    
    class Meta:
        ordering = ['-fecha_solicitud']
        verbose_name = "Cotización"
        verbose_name_plural = "Cotizaciones"

class Contacto(models.Model):
    nombre = models.CharField(max_length=100, help_text="Nombre completo de la persona de contacto",verbose_name="Nombre")
    email = models.EmailField(help_text="Correo electrónico de la persona de contacto",verbose_name="Correo Electrónico")
    telefono = models.CharField(max_length=20, help_text="Número de teléfono de la persona de contacto",verbose_name="Teléfono",
        validators=[RegexValidator(regex=r'^(\+56)?\d{9}$', message="El número de teléfono debe tener entre 9 y 15 dígitos y puede incluir el código de país.")])
    asunto = models.CharField(max_length=200, help_text="Asunto del contacto",verbose_name="Asunto")
    mensaje = models.TextField(blank=True, null=True , help_text="Mensaje adicional de la persona de contacto",verbose_name="Mensaje")
    fecha_contacto = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Contacto de {self.nombre}'
    
    class Meta:
        ordering = ['-fecha_contacto']
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"