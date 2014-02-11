# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Issue.sent'
        db.add_column(u'newsletter_issue', 'sent',
                      self.gf('django.db.models.fields.DateTimeField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Issue.sent'
        db.delete_column(u'newsletter_issue', 'sent')


    models = {
        u'newsletter.issue': {
            'Meta': {'ordering': "['-number']", 'object_name': 'Issue'},
            'end': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'sent': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'start': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'newsletter.section': {
            'Meta': {'ordering': "['position', 'name']", 'object_name': 'Section'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'position': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['newsletter']