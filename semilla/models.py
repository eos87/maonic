# -*- coding: UTF-8 -*-

from django.db import models
from encuestas.models import *

# Create your models here.

class CultivosVariedad(models.Model):
    cultivo = models.CharField(max_length=200)

    def __unicode__(self):
        return self.cultivo

    class Meta:
        verbose_name_plural = "Cultivos variedad"

class Variedades(models.Model):
    cultivo = models.ForeignKey(CultivosVariedad)
    variedad = models.CharField(max_length=200)

    def __unicode__(self):
        return '%s - %s' % (self.cultivo.cultivo, self.variedad)

    class Meta:
        verbose_name_plural = "Variedades"

CHOICE_ORIGEN = ((1,'Nativo'), (2,'Introducido'))

class UsoSemilla(models.Model):
    ''' uso de semilla
    '''
    cultivo = models.ForeignKey(Variedades, verbose_name="cultivo y su variedad",
                                help_text="Escoja el cultivo con su variedad")
    origen = models.IntegerField('Origen', choices=CHOICE_ORIGEN)
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.cultivo.cultivo
    
    class Meta:
        verbose_name_plural = "Uso de Semillas"
