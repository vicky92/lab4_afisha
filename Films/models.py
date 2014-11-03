# -*- coding: utf-8 -*-
from django.db import models
import django.db.backends.mysql

# Create your models here.

class Cinema(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    
    def __unicode__(self):
        return str(self.pk) + " " + self.name + " " + self.address
    
    
class Film(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=500)
   
    def __unicode__(self):
        return str(self.pk) + " " + self.name + " " + self.about

class Poster(models.Model):
    viewDate = models.DateTimeField()
    cinemaId = models.ForeignKey(Cinema)
    filmId   = models.ForeignKey(Film)
    
    def __unicode__(self):
        return  str(self.pk)+" " + self.cinemaId.name + " " + self.filmId.name + " " + str(self.viewDate)  