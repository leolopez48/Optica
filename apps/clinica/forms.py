from django import forms
from apps.clinica.models import *
from apps.clinica.choices import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PacienteForm(forms.ModelForm):

    class Meta:
        model = ClinicaPaciente

        fields = [
            'codpaciente',
            'nompaciente',
            'apelpaciente',
            'fechanac',
        ]

    labels = {
        'codpaciente': 'Codigo',
        'nompaciente': 'Nombre',
        'apelpaciente': 'Apellidos',
        'fechanac': 'Fecha de Nacimiento',
    }

    widgets = {
        'codpaciente': forms.TextInput(attrs={'class': 'form-control'}),
        'nompaciente': forms.TextInput(attrs={'class': 'form-control'}),
        'apelpaciente': forms.TextInput(attrs={'class': 'form-control'}),
        'fechanac': forms.TextInput(attrs={'class': 'form-control'}),
    }
    

class ConsultaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ConsultaForm, self).__init__(*args, **kwargs)
        #Sirve para modificar el tamaño del campo
        self.fields['receta'].widget.attrs.update(size = 25)
        instance = getattr(self, 'instance', None)
        if instance and instance.numconsulta:
            self.fields['fechaconsulta'].widget.attrs['readonly'] = True

    class Meta:
        model = ClinicaConsulta
        
        fields = [
            'numconsulta',
            'codpaciente',
            'coddoctor',
            'fechaconsulta',
            'enfermedad',
            'gradizq',
            'gradder',
            'receta'
        ]

    labels = {
        'numconsulta': '#',
        'codpaciente': 'Paciente',
        'coddoctor': 'Doctor',
        'fechaConsulta': 'Fecha Consulta',
        'enfermedad': 'Enfermedad',
        'gradder': 'Derecha',
        'gradizq': 'Izquierda',
        'receta': 'Receta',
    }

    widgets = {
        'numconsulta': forms.TextInput(attrs={'class': 'form-control'}),  # Field name made lowercase.
        'codpaciente': forms.Select(attrs={'class': 'browser-default custom-select'}),  # Field name made lowercase.
        'coddoctor': forms.Select(attrs={'class': 'form-control'}),  # Field name made lowercase.
        'fechaconsulta': forms.TextInput({'class': 'form-control'}),  # Field name made lowercase.  # Field name made lowercase.
        'enfermedad': forms.ChoiceField(choices=ENFERMEDAD_CHOICES, widget=forms.Select()),  # Field name made lowercase.
        'gradizq': forms.ChoiceField(choices=GRAD_CHOICES, widget=forms.Select()),
        'gradder': forms.ChoiceField(choices=GRAD_CHOICES, widget=forms.Select()),  # Field name made lowercase.
        'receta': forms.CharField(widget=forms.TextInput())
    }
