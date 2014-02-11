# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'SchedulableFeature.url'
        db.delete_column('extra_schedulablefeature', 'url')

        # Adding field 'SchedulableFeature.pointer'
        db.add_column('extra_schedulablefeature', 'pointer',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=512, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'SchedulableFeature.url'
        db.add_column('extra_schedulablefeature', 'url',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=512, blank=True),
                      keep_default=False)

        # Deleting field 'SchedulableFeature.pointer'
        db.delete_column('extra_schedulablefeature', 'pointer')


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
            'pointer': ('django.db.models.fields.URLField', [], {'max_length': '512', 'blank': 'True'}),
            'schedulable_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['chances.Schedulable']", 'unique': 'True', 'primary_key': 'True'})
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