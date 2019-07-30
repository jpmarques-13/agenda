# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContatoForm
from .models import Contato
from django.shortcuts import redirect

#import

def index (request):
    return HttpResponse('hello world')


def CriarContato (request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
        redirect('polls:VerContatos')
    else:
        form = ContatoForm()
    return render (request,'novocontato.html',{'form':form})
# Create your views here.


def VerContatos (request):
    contatos = Contato.objects.all()
    return render (request,'VerContatos.html',locals())


def EditarContatos (request,id):
    contatos = Contato.objects.get(pk=id)
    form=ContatoForm(request.POST or None,instance=contatos)
    if request.method == 'POST':
        #form = ContatoForm(request.POST, instance=contatos )
        if form.is_valid():
            form.save()
        return redirect('polls:VerContatos')
    else:
        return render (request,'editarContato.html',locals())
def deletarContatos (request,id):
    contatos = Contato.objects.get(pk=id)
    contatos.delete()
    return redirect('polls:VerContatos')
