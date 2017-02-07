from django.shortcuts import render
from django.views.generic.base import TemplateView

from vacation_request.models import RequestType


class NewRequestPageView(TemplateView):

    template_name = "requests/new_request.html"

    def get_context_data(self, **kwargs):
        context = super(NewRequestPageView, self).get_context_data(**kwargs)
        context['request_types'] = RequestType.objects.all()
        return context


class PendingRequestsPageView(TemplateView):

    template_name = "requests/pending_requests.html"

    def get_context_data(self, **kwargs):
        context = super(PendingRequestsPageView, self).get_context_data(**kwargs)
        return context


class ApprovedRequestsPageView(TemplateView):

    template_name = "requests/approved_requests.html"

    def get_context_data(self, **kwargs):
        context = super(ApprovedRequestsPageView, self).get_context_data(**kwargs)
        return context


class DeclinedRequestsPageView(TemplateView):

    template_name = "requests/declined_requests.html"

    def get_context_data(self, **kwargs):
        context = super(DeclinedRequestsPageView, self).get_context_data(**kwargs)
        return context
