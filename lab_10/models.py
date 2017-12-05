# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Pengguna(models.Model):
    kode_identitas = models.CharField('Kode Identitas', max_length=20, primary_key=True, )
    nama = models.CharField('Nama', max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class MovieKu(models.Model):
    pengguna = models.ForeignKey(Pengguna)
    kode_movie = models.CharField("Kode Movie", max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)