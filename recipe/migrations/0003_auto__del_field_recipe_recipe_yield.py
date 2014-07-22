# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Recipe.recipe_yield'
        db.delete_column(u'recipe_recipe', 'recipe_yield')


    def backwards(self, orm):
        # Adding field 'Recipe.recipe_yield'
        db.add_column(u'recipe_recipe', 'recipe_yield',
                      self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=8, decimal_places=4),
                      keep_default=False)


    models = {
        u'recipe.recipe': {
            'Meta': {'object_name': 'Recipe'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['recipe.Tag']", 'null': 'True', 'blank': 'True'})
        },
        u'recipe.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['recipe']