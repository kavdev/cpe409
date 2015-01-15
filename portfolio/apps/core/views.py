"""
.. module:: portfolio.apps.core.views
   :synopsis: Portfolio Core Views.

.. moduleauthor:: Alex Kavanaugh <kavanaugh.development@outlook.com>

"""

from django.views.generic.list import ListView

from .models import Lab


class IndexView(ListView):
    template_name = "base.html"
    model = Lab

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(kwargs)

        context["staging"] = True if "staging" in self.request.path else False

        return context


def handler500(request):
    """500 error handler which includes ``request`` in the context."""

    from django.template import RequestContext, loader
    from django.http import HttpResponseServerError

    template = loader.get_template('500.html')

    return HttpResponseServerError(template.render(RequestContext(request)))
