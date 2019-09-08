from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q

LOGIN_URL = 'http://localhost:8000/'

def basico_Nivel(view_func, redirect_field_name=REDIRECT_FIELD_NAME, login_url=LOGIN_URL):
    return user_passes_test(
        lambda u: hasattr(u, "Nivel") and u.Nivel.perfil.filter(nome="basico").exists() or u.Nivel.perfil.filter(nome="intermediario").exists() or u.Nivel.perfil.filter(nome="avancado").exists(),
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )(view_func)


def intermediario_Nivel(view_func, redirect_field_name=REDIRECT_FIELD_NAME, login_url=LOGIN_URL):
    return user_passes_test(
        lambda u: hasattr(u, "Nivel") and u.Nivel.perfil.filter(nome="intermediario").exists() or u.Nivel.perfil.filter(nome="avancado").exists(),
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )(view_func)


def avancado_Nivel(view_func, redirect_field_name=REDIRECT_FIELD_NAME, login_url=LOGIN_URL):
    return user_passes_test(
        lambda u: hasattr(u, "Nivel") and u.Nivel.perfil.filter(nome="avancado").exists(),
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )(view_func)
