# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models, connection, transaction

class Migration(DataMigration):

    def columns(self):
        return "id, name, slug, label, title, subtitle, description, datetime, display_datetime, venue_id"

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Remember to use orm['appname.ModelName'] rather than "from appname.models..."
        cursor = connection.cursor()
        cursor.execute("insert into {0}({2}) select {2} from {1}".format(
                'chances_schedulable', 'sn_schedulable', self.columns()));
        transaction.commit_unless_managed()
        

    def backwards(self, orm):
        "Write your backwards methods here."
        cursor = connection.cursor()
        cursor.execute("insert into {1}({2}) select {2} from {0}".format(
                'chances_schedulable', 'sn_schedulable', self.columns()));
        transaction.commit_unless_managed()

    models = {
        'chances.post': {
            'Meta': {'object_name': 'Post'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'published': ('django.db.models.fields.DateTimeField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
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

    complete_apps = ['chances']
    symmetrical = True
