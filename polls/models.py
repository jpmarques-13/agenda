# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from django.utils.timesince import timesince
from django.utils import timezone
from . validators import *
from django.contrib.auth.models import User
# Create your models here.


class Perfil(models.Model):
    nome = models.CharField(max_length=25, unique=True)

    @property
    def nome_formatado(self):
        return self.nome.lower().replace("_", "").replace(" ", "")

    def __unicode__(self):
        return u'%s' % self.nome



class Nivel(models.Model):
    Nome = models.OneToOneField(User, related_name='Nivel')

    perfil = models.ManyToManyField(Perfil)



class Contato(models.Model):
    Nome = models.CharField(max_length=250)
    Email = models.EmailField(null=True,validators=[validate_school_email])
    Celular =  models.CharField(max_length=14)
    Data = models.DateField(blank=True,validators=[validate_year_birtday])
    donosDeAgenda=models.ManyToManyField(User)
    cpf=models.CharField(max_length=14,unique=True,blank=True,null=True)


    @property
    def age(self):
        "retorna a idade de cada contato"
        return int((datetime.now().date()-self.Data).days/365.25)


    @property
    def tempoRestante(self):
        now = datetime.now()
        aniversario = datetime(now.year,self.Data.month,self.Data.day)
        delta = aniversario - now
        if delta.days<4 and delta.days>-4:
            return delta
        else:
            return None




