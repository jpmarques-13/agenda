# -*- coding: utf-8 -*-
import csv

from djqscsv import render_to_csv_response

from django.http import *
from django.shortcuts import render,redirect
from .forms import *
from .models import Contato
from django.contrib import messages
from django.core.paginator import Paginator, InvalidPage
from datetime import datetime
from django.db.models import Count, Max, Min
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .decorators import *
#import


def index(request):
    return render(request,'index.html')


@login_required(login_url='Usuario/login')
@basico_Nivel
def CriarContato (request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        cpf=request.POST.get('cpf')
        if form.is_valid():
            if len(Contato.objects.filter(cpf=cpf))>0:
                contatos = Contato.objects.get(cpf=cpf)
                form = ContatoForm(request.POST, instance=contatos)
                contato = form.save(commit=False)
                contato.save()
                contatos.donosDeAgenda.add(request.user)
                mensagem = "Teste123"
                messages.warning(request, mensagem)
                return redirect('polls:VerContatos')
            else:
                contato = form.save(commit=False)
                contato.cpf=cpf
                contato.save()
                mensagem = "Contato criado com sucesso"
                messages.warning(request, mensagem)
                contato.donosDeAgenda.add(request.user)
                return redirect('polls:VerContatos')
    else:
        form = ContatoForm()
    return render (request,'novocontato.html',locals())
# Create your views here.

def csv_view(request,id):
    csv=Contato.objects.all().filter(pk=id).values('Nome','Email','Celular')
    return render_to_csv_response(csv,delimiter=';',field_header_map={'Nome': 'nome',
                                                    'Email': 'email','Celular': 'celular'})

@login_required(login_url='Usuario/login')
@basico_Nivel
def VerContatos (request):
    ITEMS_PER_PAGE = 4
    page = request.GET.get('page')
    form=Filtro(request.GET or None)
    contatos=request.user.contato_set.all()
    data=datetime.now()
    if form.is_valid():
        celular=form.cleaned_data.get("celular")
        nome=form.cleaned_data.get("nome")
        if nome:
            contatos = contatos.filter(Nome__icontains=nome)
        if celular:
            contatos = contatos.filter(Celular__icontains=celular)
    paginator=Paginator(contatos,ITEMS_PER_PAGE)
    total=paginator.count
    try:
        contatos = paginator.page(page)
    except InvalidPage:
        contatos= paginator.page(1)
    return render (request,'VerContatos.html',locals())

@intermediario_Nivel
def EditarContatos (request,id):
    contatos = Contato.objects.get(pk=id)
    form=ContatoForm(request.POST or None,instance=contatos)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            mensagem = "Contato editado com sucesso"
            messages.warning(request, mensagem)
            return redirect('polls:VerContatos')
    return render (request,'editarContato.html',locals())

@avancado_Nivel
def deletarContatos (request,id):
    contatos = Contato.objects.get(pk=id)
    if request.user.contato_set.all().count()>1:
        contatos.donosDeAgenda.remove(request.user)
        mensagem = "Contato deletado com sucesso"
        messages.warning(request, mensagem)
    else:
        contatos.delete()
        mensagem = "Contato deletado com sucesso"
        messages.warning(request, mensagem)
    return redirect('polls:VerContatos')
