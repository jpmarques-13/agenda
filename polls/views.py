# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
from .models import Contato
from django.shortcuts import redirect
from django.contrib import messages
from django.core.paginator import Paginator, InvalidPage

#import

def index (request):
    return render(request,'index.html')


def CriarContato (request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            mensagem = "Contato criado com sucesso"
            messages.warning(request, mensagem)
            return redirect('polls:VerContatos')
    else:
        form = ContatoForm()
    return render (request,'novocontato.html',locals())
# Create your views here.


def VerContatos (request):
    ITEMS_PER_PAGE = 4
    page = request.GET.get('page')
    form=Filtro(request.GET or None)
    contatos=Contato.objects.all()
    if form.is_valid():
        celular=form.cleaned_data.get("celular")
        nome=form.cleaned_data.get("nome")
        if nome:
            contatos = contatos.filter(Nome=nome)
        if celular:
            contatos = contatos.filter(Celular=celular)
    paginator=Paginator(contatos,ITEMS_PER_PAGE)
    total=paginator.count
    try:
        contatos = paginator.page(page)
    except InvalidPage:
        contatos= paginator.page(1)
    return render (request,'VerContatos.html',locals())


def EditarContatos (request,id):
    contatos = Contato.objects.get(pk=id)
    form=ContatoForm(request.POST or None,instance=contatos)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            mensagem = "Contato editado com sucesso"
            messages.warning(request, mensagem)
            return redirect('polls:VerContatos')
            #form = ContatoForm(request.POST, instance=contatos )
        #return redirect('polls:VerContatos')
    return render (request,'editarContato.html',locals())
def deletarContatos (request,id):
    contatos = Contato.objects.get(pk=id)
    contatos.delete()
    mensagem = "Contato deletado com sucesso"
    messages.warning(request, mensagem)
    return redirect('polls:VerContatos')
