# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate

# Create your views here.


def novoCadastro(request):
    form=UserCreationForm(request.POST or None)
    if request.method == 'POST' :
        if form.is_valid():
            form.save()
            mensagem = "Usuario criado com sucesso"
            messages.warning ( request, mensagem)
            return redirect ( 'polls:VerContatos' )
    return render (request,'usuario.html',locals() )


def autenticacao(request):
    form=AuthenticationForm(request.POST or None)
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            mensagem = "login efetuado corretamente"
            messages.warning ( request, mensagem)
            login(request,user)
            return redirect('polls:VerContatos')
        else:
            mensagem = "login incorreto"
            messages.warning ( request, mensagem)
    return render(request,'login.html',locals())
