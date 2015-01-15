"""
.. module:: portfolio.apps.core.views
   :synopsis: Portfolio Core Views.

.. moduleauthor:: Alex Kavanaugh <kavanaugh.development@outlook.com>

"""

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Lab


class IndexView(ListView):
    template_name = "base.html"
    model = Lab


class LabView(DetailView):
    template_name = "lab_detail.html"
    model = Lab


def handler500(request):
    """500 error handler which includes ``request`` in the context."""

    from django.template import RequestContext, loader
    from django.http import HttpResponseServerError

    template = loader.get_template('500.html')

    return HttpResponseServerError(template.render(RequestContext(request)))
