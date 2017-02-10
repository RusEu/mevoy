from django.views.generic.base import TemplateView
from django.views.generic import FormView
from django.core.urlresolvers import reverse, reverse_lazy

from vacation_request.forms import RequestForm


class PendingRequestsPageView(TemplateView):
    template_name = "requests/pending_requests.html"

    def dispatch(self, *args, **kwargs):
        return super(PendingRequestsPageView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PendingRequestsPageView, self).get_context_data(**kwargs)
        context["section"] = kwargs.get('section')
        return context


class ApprovedRequestsPageView(TemplateView):
    template_name = "requests/approved_requests.html"

    def get_context_data(self, **kwargs):
        context = super(PendingRequestsPageView, self).get_context_data(**kwargs)
        context["section"] = kwargs.get('section')
        return context


class DeclinedRequestsPageView(TemplateView):
    template_name = "requests/declined_requests.html"

    def get_context_data(self, **kwargs):
        context = super(PendingRequestsPageView, self).get_context_data(**kwargs)
        context["section"] = kwargs.get('section')
        return context


class NewRequestPageView(FormView):
    template_name = "requests/new_request.html"
    form_class = RequestForm
    success_url = reverse_lazy('pending_requests')

    def get_context_data(self, **kwargs):
        context = super(NewRequestPageView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
