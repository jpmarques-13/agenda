from django.conf.urls import url

from . import views


app_name = 'polls'
urlpatterns = [
    url(r'^CriarContato$',views.CriarContato,name='CriarContato'),
    url(r'^VerContatos$',views.VerContatos,name='VerContatos'),
    url(r'^editarContatos/(?P<id>\d+)/$', views.EditarContatos, name="editar"),
    url(r'^deletarContatos/(?P<id>\d+)/$',views.deletarContatos,name='deletar'),
]
