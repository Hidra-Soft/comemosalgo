from django import forms
from .models import Comercio, Rubro
from django.forms.widgets import DateTimeInput, TextInput, CheckboxInput, CheckboxSelectMultiple, FileInput, Textarea, SelectMultiple, RadioSelect, ChoiceInput, Select
from django.forms import ModelMultipleChoiceField


RUBRO_CHOICES = (
    ('Heladeria', 'Heladeria'),
    ("Pastas", "Pastas"),
    ('Carnes', 'Carnes')
)


class ComercioRegistroForm(forms.ModelForm):
    class Meta:
        model = Comercio
        fields = (
            'nombre',
            'rubro',
            'descripcion',
            'forma_pago',
            'imagen',
            'delivery'
        )

        labels = {
            'nombre': 'Nombre del Comercio',
            'rubro': 'Rubro del Comercio',
            'descripcion': 'Descripcion del Comercio',
            'imagen': 'Seleccione imagen del logo del Comercio',
            'delivery': 'Cuenta con delivery?',
        }

        widgets = {
            'nombre': TextInput(attrs={'class': 'input-field', 'type': 'text'}),
            'rubro': SelectMultiple(),
            'descripcion': Textarea(attrs={'class': 'materialize-textarea', 'rows':20}),
            'forma_pago': SelectMultiple(),
            'imagen': FileInput(attrs={'class': 'input-field validate btn', 'type': 'file'}),
            'delivery': Select(attrs={'class': '', 'type':''}),
        }