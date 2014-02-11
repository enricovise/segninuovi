# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Section.priority'
        db.delete_column('newsletter_section', 'priority')

        # Adding field 'Section.position'
        db.add_column('newsletter_section', 'position',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding unique constraint on 'Section', fields ['name']
        db.create_unique('newsletter_section', ['name'])


    def backwards(self, orm):
        # Removing unique constraint on 'Section', fields ['name']
        db.delete_unique('newsletter_section', ['name'])

        # Adding field 'Section.priority'
        db.add_column('newsletter_section', 'priority',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Section.position'
        db.delete_column('newsletter_section', 'position')


    models = {
        'newsletter.issue': {
            'Meta': {'ordering': "['-number']", 'object_name': 'Issue'},
            'end': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'start': ('django.db.models.fields.DateField', [], {})
        },
        'newsletter.section': {
            'Meta': {'ordering': "['position', 'name']", 'object_name': 'Section'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'position': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['newsletter']