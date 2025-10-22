from django import forms
from inicio.models import Cotizacion

class CotizacionForm(forms.ModelForm):
    class Meta:
        model = Cotizacion
        fields = ['nombre', 'email', 'telefono', 'servicio', 'mensaje']
        



