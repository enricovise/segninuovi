from django.db import models

class PointerManager(models.Manager):
    def get_query_set(self):
        return super(PointerManager, self).get_query_set().exclude(url='')

class Term(models.Model):
    name = models.CharField('nome', max_length=250)

    class Meta:
        abstract = True
        verbose_name = 'termine'
        verbose_name_plural = 'termini'

    def base(self, content):
        return '<span class="term">%s</span>' % content

    def render(self, content):
        return self.base(content)

    def smartlink(self, search_term, *args, **kwargs):
        return self.render(search_term)

    def __unicode__(self):
        return self.name

class Lemma(Term):
    slug = models.SlugField(unique=True)
    url = models.URLField(blank=True, max_length=512)
    description = models.TextField('descrizione', blank=True)

    class Meta:
        verbose_name='lemma'
        verbose_name_plural='lemmi'
    
    def get_absolute_url(self):
        return self.url

    def anchor(self, content):
        return '<a href="%s">%s</a>' % (self.url, content) if self.url \
            else content

    def render(self, content):
        return self.base(self.anchor(content))

class Alias(Term):
    lemma = models.ForeignKey(Lemma, verbose_name='lemma')
    is_abbreviation = models.BooleanField('abbreviazione', default=False)

    class Meta:
        verbose_name='alias'
        verbose_name_plural='alias'

    def abbr(self, content):
        return '<abbr title="%s">%s</abbr>' % (self.lemma, content)

    def render(self, content):
        return self.base(self.lemma.anchor(
            self.abbr(content) if self.is_abbreviation else content))


class Pointer(Lemma):
    class Meta:
        proxy = True

    objects = PointerManager()
