from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from apps.clinica.views import *

urlpatterns = [
    url(r'^inicio/$', login_required(inicio), name='inicio'),
    url(r'^registrar/$', login_required(registrar), name='registrar'),
    url(r'^grafico/(?P<codpaciente>\d+)/$', login_required(grafico), name='grafico'),
    url(r'^graficoPaciente/(?P<codpaciente>\d+)/$', graficoUsuarios, name='graficoUsuarios'),
    url(r'^seleccionar/$', login_required(seleccionar), name='seleccionar'),
    url(r'^actualizar/(?P<codpaciente>\d+)/$', login_required(actualizar), name='actualizar'),
    url(r'^eliminar/(?P<codpaciente>\d+)/$', login_required(eliminar), name='eliminar'),
    url(r'^consulta/(?P<numconsulta>\d+)/$', login_required(detalle), name='detalle'),
    url(r'^nosotros/$', login_required(nosotros), name='nosotros'),
    url(r'^prueba/$', login_required(prueba), name='prueba'),
    url(r'^consulta/$', login_required(consulta), name='consulta'),
    url(r'^consulta/eliminar/(?P<numconsulta>\d+)/$', login_required(eliminarConsulta), name='eliminarConsulta'),
    url(r'^consulta/actualizar/(?P<numconsulta>\d+)/$', login_required(actualizarConsulta), name='actualizarConsulta'),
    url(r'^simulacion/miopia/$', login_required(simulacionMiopia), name='miopia'),
    url(r'^simulacion/astigmatismo/$', login_required(simulacionAstigmatismo), name='astigmatismo'),
    url(r'^simulacion/sinenfermedad/$', login_required(simulacion), name='simulacion'),
    url(r'^reporte/(?P<numconsulta>\d+)/$', login_required(reporte), name='reporte'),
    url(r'^usuarios/$', usuarios, name='usuarios'),
    url(r'^cerrar/$', cerrar, name='cerrar'),
]
