from django.shortcuts import render,redirect
from inicio.models import Servicio, Cotizacion, Contacto
from datetime import datetime
from inicio.form import CotizacionForm, ContactoForm
from django.contrib import messages
from django.http import JsonResponse


# Create your views here.

def index(request):
    servicios = Servicio.objects.all()
    anio_experiencia = datetime.now().year - 2022
    about_text = f"""Soy Julio San Martín, una persona curiosa y motivada por aprender y mejorar constantemente. Me formé como Ingeniero en Geomensura y más tarde como Técnico Analista Programador, combinando el pensamiento técnico con la lógica de la programación para crear soluciones más eficientes.

Disfruto programar, jugar ajedrez, resolver acertijos y armar el cubo Rubik, actividades que reflejan mi gusto por la lógica y los desafíos mentales. Me considero autodidacta, perseverante y observador, siempre buscando nuevas formas de aprender y aportar valor.

Creo en la mejora continua y en el poder de la tecnología para simplificar procesos y hacer las cosas un poco mejor cada día."""
    
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        if form_type == 'cotizacion':
            form = CotizacionForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Tu solicitud de cotización ha sido enviada con éxito. Nos pondremos en contacto contigo pronto.')
                return redirect('inicio')
            else:
                messages.error(request, 'Hubo un error al enviar tu solicitud. Por favor, verifica los datos e inténtalo de nuevo.')
        
        elif form_type == 'contacto':
            form_contacto = ContactoForm(request.POST)
            if form_contacto.is_valid():
                form_contacto.save()
                messages.success(request, 'Tu mensaje ha sido enviado con éxito. Nos pondremos en contacto contigo pronto.')
                return redirect('inicio')
            else:
                messages.error(request, 'Hubo un error al enviar tu mensaje. Por favor, verifica los datos e inténtalo de nuevo.')
    else:
        form = CotizacionForm()
        form_contacto = ContactoForm()
    
    
    
    
    context = {
        'servicios': servicios[:3],
        'about_text': about_text,
        'anio_experiencia': anio_experiencia,
        'form': form,
        'form_contacto': form_contacto,
    }
    return render(request, 'index.html', context)


diccionario_region_comunas = {
'Libertador General Bernardo O\'Higgins': ['Rancagua', 'Codegua', 'Coinco', 'Coltauco', 'Doñihue', 'Graneros', 'Las Cabras', 'Machalí', 'Malloa', 'Mostazal', 'Olivar', 'Peumo', 'Pichidegua', 'Quinta de Tilcoco', 'Rengo', 'Requínoa', 'San Vicente de Tagua Tagua', 'Pichilemu', 'La Estrella', 'Litueche', 'Marchihue', 'Navidad', 'Paredones', 'San Fernando', 'Chépica', 'Chimbarongo', 'Lolol', 'Nancagua', 'Palmilla', 'Peralillo', 'Placilla', 'Pumanque', 'Santa Cruz'],
'Maule': ['Talca', 'Constitución', 'Curepto', 'Empedrado', 'Maule', 'Pelarco', 'Pencahue', 'Río Claro', 'San Clemente', 'San Rafael', 'Cauquenes', 'Chanco', 'Pelluhue', 'Curicó', 'Hualañé', 'Licantén', 'Molina', 'Rauco', 'Romeral', 'Sagrada Familia', 'Teno', 'Vichuquén', 'Linares', 'Colbún', 'Longaví', 'Parral', 'Retiro', 'San Javier', 'Villa Alegre', 'Yerbas Buenas'],
'Ñuble': ['Chillán', 'Bulnes', 'Cobquecura', 'Coelemu', 'Coihueco', 'El Carmen', 'Ninhue', 'Pemuco', 'Pinto', 'Quillón', 'Quirihue', 'Ránquil', 'San Carlos', 'San Fabián', 'San Ignacio', 'San Nicolás', 'Treguaco', 'Chillán Viejo', 'Portezuelo', 'Ñiquén'],
'Biobío': ['Concepción', 'Coronel', 'Chiguayante', 'Florida', 'Hualpén', 'Hualqui', 'Lota', 'Penco', 'San Pedro de la Paz', 'Santa Juana', 'Talcahuano', 'Tomé', 'Arauco', 'Cañete', 'Contulmo', 'Curanilahue', 'Lebu', 'Los Álamos', 'Tirúa', 'Los Ángeles', 'Antuco', 'Cabrero', 'Laja', 'Mulchén', 'Nacimiento', 'Negrete', 'Quilaco', 'Quilleco', 'San Rosendo', 'Santa Bárbara', 'Tucapel', 'Yumbel', 'Alto Biobío'],
}

def obtener_regiones(request):
    regiones = list(diccionario_region_comunas.keys())
    return JsonResponse({'regiones': regiones})

def obtener_comunas_por_region(request, region):
    comunas = diccionario_region_comunas.get(region, [])
    return JsonResponse({'comunas': comunas})

