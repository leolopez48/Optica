from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from apps.paciente.views import *

urlpatterns = [
    url(r'^registrarUsuario/$', login_required(RegistroUsuario.as_view()), name='registrarUsuario'),
    url(r'^InicioPaciente/$', login_required(inicio), name='inicio'),
    url(r'^seleccionarPaciente/$', login_required(seleccionarPaciente), name='seleccionarPaciente'),
    url(r'^consulta/(?P<numconsulta>\d+)/$', detalle, name='detalle'),
    url(r'^simulacion/miopia/$', simulacionMiopia, name='miopia'),
    url(r'^simulacion/astigmatismo/$', simulacionAstigmatismo, name='astigmatismo'),
    url(r'^simulacion/sinenfermedad/$', simulacion, name='simulacion'),
]