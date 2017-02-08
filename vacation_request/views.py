from django.shortcuts import render
from django.views.generic.base import TemplateView


class NewRequestPageView(TemplateView):

    template_name = "requests/new_request.html"


class PendingRequestsPageView(TemplateView):

    template_name = "requests/pending_requests.html"


class ApprovedRequestsPageView(TemplateView):

    template_name = "requests/approved_requests.html"


class DeclinedRequestsPageView(TemplateView):

    template_name = "requests/declined_requests.html"
