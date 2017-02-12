from django.shortcuts import render
from django.views.generic.base import TemplateView

from vacation_request.models import Request, RequestType
from auth_account.models import User

from .models import Calendar


class CalendarPageView(TemplateView):

    template_name = "calendar/index.html"

    def get_context_data(self, **kwargs):
        context = super(CalendarPageView, self).get_context_data(**kwargs)
        request_type = RequestType.objects.get(id=kwargs.get('request_type'))
        section = kwargs.get('section')
        department = self.request.session['department']
        requests = Request.objects.filter(department__name=department)
        users = User.objects.filter(id=self.request.user.id)
        if section == 'manager':
            users = User.objects.filter(user_requests__request_type=request_type)
        context["requests"] = requests
        context["users"] = users
        context["section"] = section
        return context
