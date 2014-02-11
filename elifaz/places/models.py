from django.db import models
from hypertext.models import *

class Address(Lemma):
    
    class Meta:
        verbose_name = 'indirizzo'
        verbose_name_plural = 'indirizzi'

class Place(Lemma):
    address = models.ForeignKey(Address, blank=True, null=True,
                                verbose_name='indirizzo')

    class Meta:
        verbose_name = 'luogo'
        verbose_name_plural = 'luoghi'
