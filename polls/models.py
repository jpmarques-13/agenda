# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from django.utils.timesince import timesince
from django.utils import timezone
from . validators import *
from django.contrib.auth.models import User
# Create your models here.

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
