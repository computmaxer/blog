from flask import url_for

from blog import db


class Project(db.Document):
    title = db.StringField(max_length=255, required=True)
    subtitle = db.StringField(max_length=255, required=True)
    slug = db.StringField(max_length=255, required=True)
    body = db.StringField(required=True)
    comments = db.ListField(db.EmbeddedDocumentField('Comment'))

    def get_edit_url(self):
        return url_for('admin.edit-post', slug=self.slug)

    def get_absolute_url(self):
        return url_for('posts.detail', kwargs={"slug": self.slug})

    def __unicode__(self):
        return self.title

    meta = {
        'allow_inheritance': True,
        'indexes': ['slug'],
    }