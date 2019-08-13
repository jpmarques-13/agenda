# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from django.utils.timesince import timesince
from django.utils import timezone
from . validators import validate_school_email

# Create your models here.

class Contato(models.Model):
    Nome = models.CharField(max_length=250)
    Email = models.EmailField(null=True,validators=[validate_school_email])
    Celular =  models.CharField(max_length=14)
    Data = models.DateField(blank=True)
    Age = models.IntegerField(default=20)
