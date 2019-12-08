# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from apps.paciente.forms import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login


# Create your views here.

class RegistroUsuario(CreateView):
    model = User
    template_name = "paciente/registrarUsuarios.html"
    form_class = RegistroForm
    succes_url = reverse_lazy('inicio')

#A esta vista se redirecciona cuando un usuario se loggea
def inicio(request):
    if request.user.is_authenticated:
        return render(request, 'clinica/seleccionarPaciente.html')
    else:
        return render(request, 'paciente/index.html')

def login(request):
    if request.user.is_authenticated:
        return render(request, 'clinica/prueba.html')
    else:
        return render(request, 'clinica/nosotros.html')


def seleccionarPaciente(request):
    if request.user.is_authenticated:
        consulta = ClinicaConsulta.objects.all().order_by('numconsulta')
        contexto = {'consultas': consulta}
        return render(request, 'paciente/consultas.html', contexto)
    else:
        return render(request, 'clinica/nosotros.html')


def consulta(request):
    consulta = ClinicaConsulta.objects.all().order_by('numconsulta')
    contexto = {'consultas': consulta}
    return render(request, 'clinica/consultas.html', contexto)


def actualizar(request, codpaciente):
    paciente = ClinicaPaciente.objects.get(codpaciente=codpaciente)
    if request.method == 'GET':
        form = PacienteForm(instance=paciente)
    else:
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
        return redirect('seleccionar')
    return render(request, 'clinica/actualizarPacientes.html', {'form': form})

def nosotros(request):
    return render(request, 'paciente/nosotros.html')


def detalle(request, numconsulta):
    consulta = ClinicaConsulta.objects.get(numconsulta=numconsulta)
    if request.method == 'POST':
        consulta.delete()
        return redirect('consulta')
    return render(request, 'clinica/detalleConsulta.html', {'consulta': consulta})


def simulacionMiopia(request):
    return render(request, 'clinica/miopia.html')
    

def simulacionAstigmatismo(request):
    return render(request, 'clinica/astigmatismo.html')


def simulacion(request):
    return render(request, 'clinica/sinEnfermedad.html')

def cerrar(request):
    return render(request, 'clinica/index.html')

# codigo = form['codigo'].value()
#         nombre = form['nombre'].value()