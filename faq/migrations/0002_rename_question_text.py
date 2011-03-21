# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration:
    def forwards(self, orm):
        # Rename 'text' field to 'question'
        db.rename_column('faq_question', 'text', 'question')

    def backwards(self, orm):
        # Rename 'question' field to 'text'
        db.rename_column('faq_question', 'question', 'text')




