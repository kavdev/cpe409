"""
.. module:: portfolio.apps.core.admin
   :synopsis: Portfolio Core Admin Interface Configuration.

.. moduleauthor:: Alex Kavanaugh <kavanaugh.development@outlook.com>

"""

from django.contrib import admin

from .models import Lab

admin.site.register(Lab)
