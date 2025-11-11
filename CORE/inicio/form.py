from django import forms
from inicio.models import Cotizacion, Contacto

class CotizacionForm(forms.ModelForm):
    class Meta:
        model = Cotizacion
        fields = ['nombre','region','comuna', 'email', 'telefono', 'servicio', 'mensaje']
        widgets = {
            'region': forms.Select(attrs={'class': 'form-control'}),
            'comuna': forms.Select(attrs={'class': 'form-control'}),
        }
        

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'email', 'telefono', 'asunto', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control','id':'id_nombre_contacto'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','id':'id_email_contacto'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control','id':'id_telefono_contacto'}),
            'asunto': forms.TextInput(attrs={'class': 'form-control','id':'id_asunto_contacto'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control','id':'id_mensaje_contacto'}),
        }



