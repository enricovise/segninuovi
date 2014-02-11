from django.db import models
from chances.models import Schedulable, Feature

class SchedulableFeature(Schedulable, Feature):
    
    class Meta:
        verbose_name = 'evento'
        verbose_name_plural = 'eventi'
