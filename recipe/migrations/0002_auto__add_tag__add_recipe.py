# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tag'
        db.create_table(u'recipe_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'recipe', ['Tag'])

        # Adding model 'Recipe'
        db.create_table(u'recipe_recipe', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('recipe_yield', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=4)),
        ))
        db.send_create_signal(u'recipe', ['Recipe'])

        # Adding M2M table for field tags on 'Recipe'
        m2m_table_name = db.shorten_name(u'recipe_recipe_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recipe', models.ForeignKey(orm[u'recipe.recipe'], null=False)),
            ('tag', models.ForeignKey(orm[u'recipe.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['recipe_id', 'tag_id'])


    def backwards(self, orm):
        # Deleting model 'Tag'
        db.delete_table(u'recipe_tag')

        # Deleting model 'Recipe'
        db.delete_table(u'recipe_recipe')

        # Removing M2M table for field tags on 'Recipe'
        db.delete_table(db.shorten_name(u'recipe_recipe_tags'))


    models = {
        u'recipe.recipe': {
            'Meta': {'object_name': 'Recipe'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'recipe_yield': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '4'}),
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