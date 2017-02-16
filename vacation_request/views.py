from django.utils.translation import ugettext_lazy as _
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseForbidden

from vacation_request.models import Request
from vacation_request.forms import RequestForm
from notifications.models import Notification


class PendingRequestsPageView(TemplateView):
    template_name = "requests/pending_requests.html"

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(PendingRequestsPageView, self).dispatch(*args, **kwargs)

    def notify_user(self, vacation_request):
        message = _("Department: {} has {} your request".format(
            vacation_request.department.name, vacation_request.status))
        Notification.objects.create(user=vacation_request.user, message=message)

    def post(self, request, *args, **kwargs):
        data = request.POST
        if request.session.get('is_manager'):
            obj = Request.objects.get(id=data.get("request"))
            if not request.session["department"] == obj.department.name:
                return HttpResponseForbidden()
            method = data["method"]
            if method == 'approve':
                obj.status = obj.APPROVED
            elif method == 'decline':
                obj.status = obj.DECLINED
            else:
                return HttpResponseForbidden()
            self.notify_user(vacation_request=obj)
            obj.save()
            return HttpResponse(status=200)
        return HttpResponseForbidden()


class ApprovedRequestsPageView(TemplateView):
    template_name = "requests/approved_requests.html"


class DeclinedRequestsPageView(TemplateView):
    template_name = "requests/declined_requests.html"


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
