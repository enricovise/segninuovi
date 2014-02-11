from sn.models import *
from django.contrib.admin import site, ModelAdmin, TabularInline, StackedInline
import models
from hypertext.admin import *
from django.conf import settings

class AuthorshipInline(TabularInline):
  model = Person.materials.through
  extra = 1

class MaterialAdmin(ModelAdmin):
  inlines = [AuthorshipInline,]

class PersonAdmin(ModelAdmin):
  list_display = ('__unicode__', 'first_name', 'last_name')
  inlines = [AuthorshipInline,]
  exclude = ('materials',)

class UserAdmin(ModelAdmin):
  list_display = ('username', 'first_name', 'last_name')


class CommonMedia:
  js = (
    'https://ajax.googleapis.com/ajax/libs/dojo/1.6.0/dojo/dojo.xd.js',
    '%seditor.js' % settings.STATIC_URL,
  )
  css = {
    'all': ('%seditor.css' % settings.STATIC_URL,),
  }

class OrganizationAdmin(ModelAdmin):
  inlines = [AliasInline,]


site.unregister(User)
site.register(User, UserAdmin, Media=CommonMedia,)
site.register(Person, PersonAdmin, Media=CommonMedia,)
site.register(Material, MaterialAdmin)
site.register(Organization, OrganizationAdmin)
