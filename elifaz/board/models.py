from django.db import models
from chances.models import Post
from scuoladsc.models import Edition, Module, Reference
import chances
import extra
from django.core.urlresolvers import reverse


class Feature(Post, chances.models.Feature):
    
    class Meta:
        verbose_name = 'risorsa extra'
        verbose_name_plural = 'risorse extra'
        

class SchedulableFeature(Post):
    schedulable_feature = models.ForeignKey(extra.models.SchedulableFeature,
                                            verbose_name='evento extra')
    
    def get_absolute_url(self):
        return self.schedulable_feature.get_absolute_url()
        
    class Meta:
        verbose_name = 'evento extra'
        verbose_name_plural = 'eventi extra'


class SchoolEdition(Post):
    edition = models.ForeignKey(Edition, verbose_name='edizione')
    
    def get_absolute_url(self):
        return self.get_full_url(self.edition.get_absolute_url())
    
    class Meta:
        verbose_name = 'edizione della scuola'
        verbose_name_plural = 'edizioni della scuola'


class SchoolModule(Post):
    module = models.ForeignKey(Module, verbose_name='modulo')

    def get_absolute_url(self):
        return self.get_full_url(self.module.get_absolute_url())
        
    class Meta:
        verbose_name = 'modulo della scuola'
        verbose_name_plural = 'moduli della scuola'


class SchoolReference(Post):
    reference = models.ForeignKey(Reference,
                                  verbose_name='materiale')
    
    def get_absolute_url(self):
        return self.get_full_url(self.reference.get_absolute_url())

    class Meta:
        verbose_name = 'materiale della scuola'
        verbose_name_plural = 'materiali della scuola'
    
