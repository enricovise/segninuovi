from hypertext.models import *
from django.contrib.admin import site, ModelAdmin, TabularInline
import models

class AliasInline(TabularInline):
    model = Alias

class LemmaAdmin(ModelAdmin):
    list_display = ('name', )
    inlines = [AliasInline, ]

site.register(Lemma, LemmaAdmin)
site.register(Alias)
