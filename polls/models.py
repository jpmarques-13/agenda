# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from django.utils.timesince import timesince
from django.utils import timezone

# Create your models here.

class Contato(models.Model):
    Nome = models.CharField(max_length=250)
    Email = models.EmailField()
    Celular =  models.CharField(max_length=14)
    Data = models.DateField(blank=True)
