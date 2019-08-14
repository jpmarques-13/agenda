from django.conf.urls import url
from . import views


app_name = 'autenticacao'
urlpatterns = [
    url(r'^novoUsuario$',views.novoCadastro,name='novoCadastro'),
]
