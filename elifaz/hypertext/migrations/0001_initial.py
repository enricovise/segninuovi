# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Lemma'
        db.create_table('hypertext_lemma', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=512, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('hypertext', ['Lemma'])

        # Adding model 'Alias'
        db.create_table('hypertext_alias', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('lemma', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hypertext.Lemma'])),
            ('is_abbreviation', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('hypertext', ['Alias'])


    def backwards(self, orm):
        # Deleting model 'Lemma'
        db.delete_table('hypertext_lemma')

        # Deleting model 'Alias'
        db.delete_table('hypertext_alias')


    models = {
        'hypertext.alias': {
            'Meta': {'object_name': 'Alias'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_abbreviation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lemma': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hypertext.Lemma']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'hypertext.lemma': {
            'Meta': {'object_name': 'Lemma'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '512', 'blank': 'True'})
        }
    }

    complete_apps = ['hypertext']