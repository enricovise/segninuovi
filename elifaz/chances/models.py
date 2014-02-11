from django.db import models
from places.models import Place
from newsletter.models import Section
from model_utils.managers import InheritanceManager
from django.contrib.sites.models import Site

class Note(models.Model):
    name = models.CharField('nome', max_length=255, help_text="Per uso interno")
    slug = models.SlugField(help_text="Per l'indirizzo internet")
    title = models.CharField('titolo', max_length=255, blank=True)
    subtitle = models.CharField('sottotitolo', max_length=255, blank=True)
    description = models.TextField('descrizione', blank=True)

    class Meta:
        abstract = True


class Feature(models.Model):
    url = models.URLField(max_length=512)

    def get_absolute_url(self):
        return self.url
    
    class Meta:
        abstract = True


class PostManager(InheritanceManager):
    def published_range(self, start, end):
        return super(PostManager, self).get_query_set().filter(
                published__range=(start, end)).order_by('label__position',
                                           '-published').select_subclasses()

class Post(Note):
    label = models.ForeignKey(Section, verbose_name='sezione')
    published = models.DateTimeField('pubblicazione', blank=False)
    objects = PostManager()

    def get_full_url(self, absolute_url):
        return "http://{0}{1}".format(Site.objects.get_current(), absolute_url)

    class Meta:
        ordering = ['-published', 'slug']


class Schedulable(Note):
    SEPARATOR = '/'
    label = models.CharField('etichetta', max_length=255, blank=True)
    datetime = models.DateTimeField('inizio', blank=True, null=True)
    display_datetime = models.BooleanField('visualizza data/ora di inizio', default=True)
    venue = models.ForeignKey(Place, blank=True, null=True, related_name='held',
                              verbose_name='luogo')

    class Meta:
        ordering = ['datetime', 'slug',]

    def __unicode__(self):
        return '%s (%s)' % (self.name,
                            self.SEPARATOR.join(
                             [x.slug for x in self.ancestors()] + [self.slug]))

    def parent(self):
        return None

    def get_children(self, related):
        return getattr(self, related).all()

    def ancestors(self):
        return self.parent().ancestors() + [self.parent()] if self.parent() \
            else []

    def path(self):
        return self.SEPARATOR.join([x.slug for x in self.ancestors()])

    def tags(self):
        return [("label", self.label), ("title", self.title),
                ("subtitle", self.subtitle), ("description", self.description)]
    
    def nonvoid_tags(self):
        def collapse(list):
            return [x for x in list if x[1]]
        
        return collapse(self.tags()) if collapse(self.tags()) else \
            [("name", self.name)]
