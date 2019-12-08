# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from apps.clinica.forms import *


# Create your views here.

def inicio(request):
    return render(request, 'clinica/Inicio.html')


def seleccionar(request):
    paciente = ClinicaPaciente.objects.all()
    contexto = {'pacientes': paciente}
    return render(request, 'clinica/seleccionarPaciente.html', contexto)


def consulta(request):
    consulta = ClinicaConsulta.objects.all().order_by('numconsulta')
    contexto = {'consultas': consulta}
    return render(request, 'clinica/consultas.html', contexto)


def registrar(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prueba')
    else:
        form = PacienteForm()
    return render(request, 'clinica/registrarPacientes.html', {'form': form})


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


def eliminar(request, codpaciente):
    paciente = ClinicaPaciente.objects.get(codpaciente=codpaciente)
    if request.method == 'POST':
        paciente.delete()
        return redirect('seleccionar')
    return render(request, 'clinica/eliminarPaciente.html', {'paciente': paciente})


def nosotros(request):
    return render(request, 'clinica/nosotros.html')


def prueba(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consulta')
    else:
        form = ConsultaForm()
    return render(request, 'clinica/prueba.html', {'form': form})


def detalle(request, numconsulta):
    consulta = ClinicaConsulta.objects.get(numconsulta=numconsulta)
    if request.method == 'POST':
        consulta.delete()
        return redirect('consulta')
    return render(request, 'clinica/detalleConsulta.html', {'consulta': consulta})


def eliminarConsulta(request, numconsulta):
    consulta = ClinicaConsulta.objects.get(numconsulta=numconsulta)
    if request.method == 'POST':
        consulta.delete()
        return redirect('consulta')
    return render(request, 'clinica/eliminarConsulta.html', {'consulta': consulta})

def actualizarConsulta(request, numconsulta):
    consulta = ClinicaConsulta.objects.get(numconsulta=numconsulta)
    if request.method == 'GET':
        form = ConsultaForm(instance=consulta)
    else:
        form = ConsultaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
        return redirect('consulta')
    return render(request, 'clinica/actualizarConsulta.html', {'form': form})


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
