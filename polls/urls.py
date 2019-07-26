from django.conf.urls import url

from . import views


app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^CriarContato$',views.CriarContato,name='CriarContato'),
    url(r'^VerContatos$',views.VerContatos,name='VerContatos'),
]
