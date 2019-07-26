# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContatoForm
from .models import Contato
def index (request):
    return HttpResponse('hello world')
def CriarContato (request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContatoForm()
    return render (request,'novocontato.html',{'form':form})
# Create your views here.
def VerContatos (request):
    contatos = Contato.objects.all()
    return render (request,'VerContatos.html',{'contatos':contatos})
