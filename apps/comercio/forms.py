from django import forms
from .models import Comercio
from django.forms.widgets import DateTimeInput, TextInput, CheckboxInput, CheckboxSelectMultiple, FileInput, Textarea


class ComercioRegistroForm(forms.ModelForm):
    class Meta:
        model = Comercio
        fields = (
            'nombre',
            'rubro',
            'horarios',
            'descripcion',
            'forma_pago',
            'imagen',
            'delivery',
        )

        labels = {
            'nombre': 'Nombre del Comercio',
            'rubro': 'Rubro del Comercio',
            'horarios': 'Horarios del Comercio',
            'descripcion': 'Descripcion del Comercio',
            'imagen': 'Seleccione imagen del logo del Comercio',
            'delivery': 'Cuenta con delivery?',
        }

        widgets = {
            'nombre': TextInput(attrs={'class': 'form-control'}),
            'rubro': TextInput(attrs={'class': 'form-control'}),
            'horarios': DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}),
            'descripcion': Textarea(attrs={'class': 'form-control', 'rows':10}),
            'forma_pago': CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'imagen': FileInput(attrs={'class': 'form-control'}),
            'delivery': CheckboxInput(attrs={'class': 'form-control', 'type': ''}),
        }