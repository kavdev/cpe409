"""
.. module:: portfolio.apps.core.views
   :synopsis: Portfolio Core Views.

.. moduleauthor:: Alex Kavanaugh <kavanaugh.development@outlook.com>

"""

from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "base.html"


def handler500(request):
    """500 error handler which includes ``request`` in the context."""

    from django.template import RequestContext, loader
    from django.http import HttpResponseServerError

    template = loader.get_template('500.html')

    return HttpResponseServerError(template.render(RequestContext(request)))
