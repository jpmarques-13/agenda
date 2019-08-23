from django.forms import ModelForm, ValidationError
from django import forms
from .models import Contato
from django.core import validators
from .validators import *


class ContatoForm(ModelForm):
    cpf = forms.CharField(max_length=14)
    class Meta:
        model  = Contato
        fields = ['Nome','Email','Celular','Data',]
    Data = forms.DateField(
        widget=forms.DateInput(format='%m/%d/%Y'),
        input_formats=('%m/%d/%Y',),
    )
    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        return cpf


class Filtro(forms.Form):
    nome = forms.CharField(label=u'Nome', max_length=250, widget=forms.TextInput(
    attrs={'class': 'form-control'}), required=False)
    celular = forms.CharField(label=u'Celular', max_length=14, widget=forms.TextInput(
    attrs={'class': 'form-control'}), required=False)
