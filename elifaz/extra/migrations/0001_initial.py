# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SchedulableFeature'
        db.create_table('extra_schedulablefeature', (
            ('schedulable_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['chances.Schedulable'], unique=True, primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=512, blank=True)),
        ))
        db.send_create_signal('extra', ['SchedulableFeature'])


    def backwards(self, orm):
        # Deleting model 'SchedulableFeature'
        db.delete_table('extra_schedulablefeature')


    models = {
        'chances.schedulable': {
            'Meta': {'ordering': "['datetime', 'slug']", 'object_name': 'Schedulable'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'display_datetime': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'held'", 'null': 'True', 'to': "orm['places.Place']"})
        },
        'extra.schedulablefeature': {
            'Meta': {'ordering': "['datetime', 'slug']", 'object_name': 'SchedulableFeature', '_ormbases': ['chances.Schedulable']},
            'schedulable_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['chances.Schedulable']", 'unique': 'True', 'primary_key': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '512', 'blank': 'True'})
        },
        'hypertext.lemma': {
            'Meta': {'object_name': 'Lemma'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '512', 'blank': 'True'})
        },
        'places.address': {
            'Meta': {'object_name': 'Address', '_ormbases': ['hypertext.Lemma']},
            'lemma_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['hypertext.Lemma']", 'unique': 'True', 'primary_key': 'True'})
        },
        'places.place': {
            'Meta': {'object_name': 'Place', '_ormbases': ['hypertext.Lemma']},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['places.Address']", 'null': 'True', 'blank': 'True'}),
            'lemma_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['hypertext.Lemma']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['extra']