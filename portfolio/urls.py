"""
.. module:: portfolio.urls
   :synopsis: Portfolio URLs.

.. moduleauthor:: Alex Kavanaugh <kavanaugh.development@outlook.com>

"""

import logging

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.defaults import permission_denied, page_not_found
from django.views.generic.base import RedirectView

from .apps.core.views import IndexView, handler500

admin.autodiscover()

logger = logging.getLogger(__name__)

handler500 = handler500

# Core
urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^bitbucket/$', RedirectView.as_view(url="https://bitbucket.org/kavanaugh_development/cpe409/"), name='bitbucket'),
    url(r'^flugzeug/', include(admin.site.urls)),  # admin site urls, masked
)

# Lab display
# urlpatterns += [
#     url(r'^labs/$', LabsView.as_view()), name='labs'),
# ]

# Hooks to intentionally raise errors
urlpatterns += [
    url(r'^500/$', handler500, name="500"),
    url(r'^403/$', permission_denied, name="403"),
    url(r'^404/$', page_not_found, name="404"),
]