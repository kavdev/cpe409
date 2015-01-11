"""
.. module:: portfolio.apps.core.models
   :synopsis: Portfolio Core Models.

.. moduleauthor:: Alex Kavanaugh <kavanaugh.development@outlook.com>

"""

from django.db.models.base import Model
from django.db.models.fields import CharField


class Lab(Model):

    title = CharField(max_length=30, verbose_name="Title")
    slug = CharField(max_length=10, verbose_name="Codepen Slug")

    def __str__(self):
        return self.title + " - " + self.slug
