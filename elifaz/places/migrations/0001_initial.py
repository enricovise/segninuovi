# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Address'
        db.create_table('places_address', (
            ('lemma_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['hypertext.Lemma'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('places', ['Address'])

        # Adding model 'Place'
        db.create_table('places_place', (
            ('lemma_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['hypertext.Lemma'], unique=True, primary_key=True)),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.Address'], null=True, blank=True)),
        ))
        db.send_create_signal('places', ['Place'])


    def backwards(self, orm):
        # Deleting model 'Address'
        db.delete_table('places_address')

        # Deleting model 'Place'
        db.delete_table('places_place')


    models = {
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

    complete_apps = ['places']