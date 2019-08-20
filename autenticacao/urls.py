from django.conf.urls import url
from . import views


app_name = 'autenticacao'

urlpatterns = [
    url(r'^novoUsuario/$',views.novoCadastro,name='novoCadastro'),
    url(r'^login/$',views.autenticacao,name='autenticacao'),
    url(r'^logout/$',views.logout_view,name='logout_view'),
]
