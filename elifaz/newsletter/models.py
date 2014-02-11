#!/usr/bin/python
# coding: latin-1

from django.db import models
from mailsnake import MailSnake
from mailsnake.exceptions import *
from datetime import datetime
from django.template.loader import render_to_string
from django.template import Context
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.utils import timezone
from elifaz import settings

class Section(models.Model):
    name = models.CharField('nome', max_length=50, unique=True)
    position = models.IntegerField('posizione', blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'sezione'
        verbose_name_plural = 'sezioni'
        ordering = ['position', 'name']

        
class MyMailSnake(MailSnake):
    def __init__(self, apikey):
        super(MyMailSnake, self).__init__(apikey)
        self.apikey = apikey

    def send(self, list_id, email_address, type, opts, content):
        self.listMemberInfo(id=list_id, email_address=email_address)
        return self.campaignSendNow(apikey=self.apikey,
            cid=self.campaignCreate(type=type, options=opts, content=content))


from chances.models import Post

class Issue(models.Model):
    number = models.IntegerField('numero', unique=True)
    start = models.DateTimeField('da')
    end = models.DateTimeField('a')
    last_sent = models.DateTimeField('ultimo invio', null=True)

    def formatted_number(self):
        return "{0:03d}".format(self.number)
    
    def formatted_title(self):
        return 'Newsletter #{0}'.format(self.number) # &#8470;

    def __unicode__(self):
        return "{0}".format(self.formatted_number())

    def get_absolute_url(self):
        return reverse('issue_detail', kwargs={'number': self.number})
    
    def sent(self):
        return self.last_sent != None

    sent.boolean = True
    sent.short_description = 'inviata'

    def opts(self):
        opts = {'list_id': settings.MAILCHIMP_LIST_ID}
        opts['subject']=self.__unicode__() + ' ' + timezone.now().strftime(
            '%d %B %Y, %H.%M.%S')
        opts['from_email']='enricovise@gmail.com'
        opts['from_name']='Mr Enrico Visentini'
        opts['tracking']={'opens': True, 'html_clicks': True,
                          'text_clicks': False}
        opts['authenticate'] = True
        opts['title'] = 'Test ' + timezone.now().strftime('%d %B %Y, %H.%M.%S')
        return opts
        
    def context(self):
        return Context({'issue': self,
                        'post_list': Post.objects.published_range(self.start,
                                                                  self.end)})

    def content(self):
        return {'html': render_to_string('newsletter/issue_detail_email.html',
                                         self.context()),
                'text': 'Plain text: Ecco!',}

    def send(self):
        sent = MyMailSnake(settings.MAILCHIMP_APIKEY).send(
            settings.MAILCHIMP_LIST_ID, 'enricovise@gmail.com', 'regular',
                                                    self.opts(), self.content())
        if sent:
            self.last_sent = timezone.now()
            self.save()
        return sent

    class Meta:
        verbose_name = 'edizione'
        verbose_name_plural = 'edizioni'
        ordering = ['-number']
