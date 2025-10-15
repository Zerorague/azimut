from django.shortcuts import render
from inicio.models import Servicio
from datetime import datetime

# Create your views here.

def index(request):
    servicios = Servicio.objects.all()
    anio_experiencia = datetime.now().year - 2021
    about_text = f"""En Azimut nos especializamos en brindar soluciones topográficas integrales con los más altos estándares de calidad.
      Nuestro equipo de profesionales cuenta con más de {anio_experiencia} años de experiencia en el sector, 
      utilizando tecnología de punta para garantizar resultados precisos y confiables en cada proyecto. 
      Nos comprometemos a ofrecer un servicio personalizado, adaptándonos a las necesidades específicas de cada cliente."""
    
    context = {
        'servicios': servicios[:3],
        'about_text': about_text,
        'anio_experiencia': anio_experiencia
    }
    return render(request, 'index.html', context)