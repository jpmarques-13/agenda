from django.forms import ModelForm
from django import forms
from .models import Contato


class ContatoForm(ModelForm):
    class Meta:
        model=Contato
        fields=['Nome','Email','Celular','Data','Age']
    Data=forms.DateField(
        widget=forms.DateInput(format='%m/%d/%Y'),
        input_formats=('%m/%d/%Y',),
    )
class Filtro(forms.Form):
    nome=forms.CharField(label=u'Nome', max_length=250, widget=forms.TextInput(
        attrs={'class': 'form-control'}), required=False)
    celular=forms.CharField(label=u'Celular', max_length=14, widget=forms.TextInput(
        attrs={'class': 'form-control'}), required=False)
