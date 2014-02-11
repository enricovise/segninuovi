from django.db import models
from chances.models import Schedulable
from sn.models import Person, Material
from django.db.models import Q
from elifaz import settings
from django.core.urlresolvers import reverse

class Edition(Schedulable):
    def get_references(self):
        return sorted(Reference.objects.filter(
            Q(speaker__call__module__edition=self) |
            Q(call__module__edition=self)),
                  key=lambda reference: reference.material.get_author_string())

    def get_absolute_url(self):
        return reverse('edition_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'edizione'
        verbose_name_plural = 'edizioni'



class Module(Schedulable):
    edition = models.ForeignKey(Edition, verbose_name='edizione')

    def parent(self):
        return self.edition

    def get_absolute_url(self):
        return self.parent().get_absolute_url()
        
    class Meta:
        verbose_name = 'modulo'
        verbose_name_plural = 'moduli'

    
class Call(Schedulable):
    module = models.ForeignKey(Module, verbose_name='modulo')

    def parent(self):
        return self.module

    class Meta:
        verbose_name = 'intervento'
        verbose_name_plural = 'interventi'


class Speaker(Schedulable):
    call = models.ForeignKey(Call, verbose_name='intervento')
    person = models.ForeignKey(Person, verbose_name='persona')

    class Meta:
        verbose_name = 'relatore'
        verbose_name_plural = 'relatori'

    def parent(self):
        return self.call

class Reference(Schedulable):
    call = models.ForeignKey(Call, blank=True, null=True,
                             verbose_name='intervento')
    speaker = models.ForeignKey(Speaker, blank=True, null=True,
                                verbose_name='relatore')
    material = models.ForeignKey(Material, verbose_name='materiale')

    def parent(self):
        return self.speaker or self.call

    def get_absolute_url(self):
        return "{0}{1}".format(settings.MEDIA_URL, self.material.file.file)
    
    def get_module(self):
        return self.speaker.call.module.label if self.speaker.call.module else \
            self.call.module.label
    
    class Meta:
        verbose_name = 'riferimento'
        verbose_name_plural = 'riferimenti'


