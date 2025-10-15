from django.db import models
from django_resized import ResizedImageField

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
        return self.nombre