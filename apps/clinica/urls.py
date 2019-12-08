from django.conf.urls import url

from apps.clinica.views import *

urlpatterns = [
    url(r'^Inicio/$', inicio, name='inicio'),
    url(r'^registrar/$', registrar, name='registrar'),
    url(r'^seleccionar/$', seleccionar, name='seleccionar'),
    url(r'^actualizar/(?P<codpaciente>\d+)/$', actualizar, name='actualizar'),
    url(r'^eliminar/(?P<codpaciente>\d+)/$', eliminar, name='eliminar'),
    url(r'^consulta/(?P<numconsulta>\d+)/$', detalle, name='detalle'),
    url(r'^nosotros/$', nosotros, name='nosotros'),
    url(r'^prueba/$', prueba, name='prueba'),
    url(r'^consulta/$', consulta, name='consulta'),
    url(r'^consulta/eliminar/(?P<numconsulta>\d+)/$', eliminarConsulta, name='eliminarConsulta'),
    url(r'^consulta/actualizar/(?P<numconsulta>\d+)/$', actualizarConsulta, name='actualizarConsulta'),
    url(r'^simulacion/miopia/$', simulacionMiopia, name='miopia'),
    url(r'^simulacion/astigmatismo/$', simulacionAstigmatismo, name='astigmatismo'),
    url(r'^simulacion/sinenfermedad/$', simulacion, name='simulacion'),
]