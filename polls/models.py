# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Contato(models.Model):
    Nome = models.CharField(max_length=250)
    Email = models.EmailField()
    Celular =  models.CharField(max_length=11)
    
