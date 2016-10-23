from django import forms
from apps.comercio.models import Departamento


class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = [
            'codigo',
            'nombre',
        ]

        labels = {
            'codigo': 'Codigo departamento',
            'nombre': 'Nombre departamento'
        }

        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }