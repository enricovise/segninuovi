from django.db import models
from django.contrib.auth.models import User 
from filer.fields.file import FilerFileField
from hypertext.models import Lemma
from places.models import Place
from operator import itemgetter, attrgetter
from django.core.urlresolvers import reverse

class Resource(models.Model):
    slug = models.SlugField(max_length=50)

    def __unicode__(self):
        return self.slug

class Person(Resource):
    TITLE = (
        ('Mons.', 'Monsignore'),
        ('S.E. Mons.', 'Vescovo'),
        ('S.Em. Card.', 'Cardinale'),
    )
    title = models.CharField('titolo',
                             blank=True, max_length=15, choices = TITLE)
    first_name = models.CharField('nome', max_length=30)
    last_name = models.CharField('cognome', max_length=50)
    biography = models.TextField('cenni biografici', blank=True)
    organization = models.ForeignKey("Organization", blank=True, null=True,
                                     verbose_name='organizzazione')
    materials = models.ManyToManyField("Material", related_name="authors",
                                       through='Attribution',
                                       verbose_name='materiali')
    user = models.ForeignKey(User, null=True, blank=True, default=None,
                             verbose_name='utente')

    class Meta:
        verbose_name = 'persona'
        verbose_name_plural = 'persone'

    def get_title_and_first_name(self):
        return " ".join([self.title, self.first_name]).strip()

    def __unicode__(self):
        return " ".join([self.title, self.first_name, self.last_name]).strip()
    
    def get_name(self):
        return " ".join([self.get_title_and_first_name().replace(' ', '&nbsp;'),
                         self.last_name])

    def get_neighborhood(self, radius):
        people = list(Person.objects.all().order_by('last_name',
                                                    'first_name'))
        centre = people.index(self)
        return people[max(0,min(centre-radius,len(people)-(1+2*radius))):max(2*radius,centre+radius)+1]

    def get_absolute_url(self):
        return reverse('person_detail', kwargs={'slug': self.slug})


class Material(Resource):
    file = FilerFileField(null=False, blank=False)
    date = models.DateField('data', null=True, blank=True)

    class Meta:
        verbose_name='materiale'
        verbose_name_plural='materiali'

    def __unicode__(self):
        return self.file.name if self.file.name else self.file.url

    def get_sorted_author_list(self):
        return sorted(list(self.authors.all()), key=attrgetter('last_name',
                                                               'first_name'))

    def get_author_string(self):
        return " ".join(['%s,&thinsp;%s.' % (author.last_name,
                                             author.first_name[0]) \
                             for author in self.get_sorted_author_list()])


class Organization(Lemma):

    class Meta:
        verbose_name='organizzazione'
        verbose_name_plural='organizzazioni'


class Attribution(models.Model):
    person = models.ForeignKey(Person, verbose_name='persona')
    material = models.ForeignKey(Material, verbose_name='materiale')
    
    class Meta:
        verbose_name='attribuzione'
        verbose_name_plural='attribuzioni'
