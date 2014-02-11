#!/usr/bin/python
# -*- coding: utf-8 -*-

from newsletter.models import *
from django.contrib.admin import site, ModelAdmin
from django.utils import timezone
import sys

class IssueAdmin(ModelAdmin):
    actions = ['send']
    
    list_display = ('__unicode__', 'start', 'end', 'sent', 'last_sent')

    def send(self, request, queryset):
        if queryset.count() > 1:
            self.message_user(request, "Selezionare una sola edizione alla " + \
                              "volta. Nessuna edizione è stata pubblicata.")
            return
    
        try:
            sent = queryset[0].send()
        except:
            self.message_user(request, sys.exc_info()[0])
        else:
            self.message_user(request, "L'edizione è stata inviata." \
                              if sent else "Si è verificato un errore. " + \
                              "L'edizione non è stata inviata.")

    send.short_description = "Invia edizione selezionata"


                

site.register(Issue, IssueAdmin)
site.register(Section)
