# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages

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
