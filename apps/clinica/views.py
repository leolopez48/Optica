# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from apps.clinica.forms import *
from django.core.exceptions import MultipleObjectsReturned
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
from django.views.generic import View
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.db.models import Q #Libreria para realizar barra de busqueda


# Create your views here.

def seleccionar(request):
    queryset = request.GET.get("buscar")
    if queryset:
        paciente = ClinicaPaciente.objects.filter(
            Q(codpaciente = queryset)
            )
    else:
        paciente = ClinicaPaciente.objects.all()
    contexto = {'pacientes': paciente}
    return render(request, 'clinica/seleccionarPaciente.html', contexto)

def usuarios(request):
   queryset = request.GET.get("buscar")
   if queryset:
      paciente = ClinicaPaciente.objects.filter(Q(codpaciente = queryset))
      contexto = {'pacientes': paciente}
      return render(request, 'clinica/usuarios.html', contexto)
   return render(request, 'clinica/usuarios.html')


def inicio(request):
    return render(request, 'clinica/Inicio.html')


def consulta(request):
   queryset = request.GET.get("buscar")
   if(queryset):
      consulta= ClinicaConsulta.objects.filter(Q(codpaciente = queryset)).distinct()
   else:
      consulta = ClinicaConsulta.objects.all().order_by('numconsulta')
   contexto = {'consultas': consulta}
   return render(request, 'clinica/consultas.html', contexto)


def grafico(request, codpaciente):
    consulta = ClinicaConsulta.objects.filter(codpaciente=codpaciente).order_by('numconsulta')
    consultas = {'consultas':consulta}
    return render(request,'clinica/grafico.html',consultas)


def graficoUsuarios(request, codpaciente):
    consulta = ClinicaConsulta.objects.filter(codpaciente=codpaciente).order_by('numconsulta')
    consultas = {'consultas':consulta}
    return render(request,'clinica/graficoUsuarios.html',consultas)


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

def render_pdf(url_template, contexto={}):
    template = get_template(url_template)
    html = template.render(contexto)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type="application/pdf")

    return None

def reporte(request, numconsulta):
    consulta = ClinicaConsulta.objects.get(numconsulta=numconsulta)
    pdf = render_pdf("clinica/reporte.html", {'consulta': consulta})
    return HttpResponse(pdf, content_type="application/pdf")


# codigo = form['codigo'].value()
#         nombre = form['nombre'].value()
