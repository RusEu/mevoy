from django.shortcuts import render
from django.views.generic.base import TemplateView

from vacation_request.models import Request, RequestType
from auth_account.models import User

from .models import Calendar


class CalendarPageView(TemplateView):

    template_name = "calendar/index.html"

    def get_context_data(self, **kwargs):
        context = super(CalendarPageView, self).get_context_data(**kwargs)
        context["request_types"] = RequestType.objects.all()
        return context
