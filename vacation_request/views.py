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
        """
        :return: HttpResponseForbidden if user is not manager or users's
                 department is not the same as the request department or
                 the action is not decline or approve.
                 HttpResponse with 200 status if the request has been modified.
        """
        data = request.POST
        action = data.get('action')
        obj = Request.objects.get(id=data.get("request"))
        if request.user not in obj.department.managers.all():
            return HttpResponseForbidden()
        if action not in ('approve', 'decline',):
            return HttpResponseForbidden()

        if action == 'approve':
            requested_approvals = obj.request_type.approvals
            obj.approvals.add(self.request.user)
            if obj.department.managers.count() >= requested_approvals:
                if obj.approvals.count() == requested_approvals:
                    obj.status = obj.APPROVED
            else:
                obj.status = obj.APPROVED
        elif action == 'decline':
            obj.status = obj.DECLINED
        self.notify_user(vacation_request=obj)
        obj.save()
        return HttpResponse(status=200)


class ApprovedRequestsPageView(TemplateView):
    template_name = "requests/approved_requests.html"


class DeclinedRequestsPageView(TemplateView):
    template_name = "requests/declined_requests.html"


class NewRequestPageView(FormView):
    template_name = "requests/new_request.html"
    form_class = RequestForm
    success_url = reverse_lazy('pending_requests')

    def get_form(self):
        if self.request.POST:
            data = self.request.POST.copy()
            data["user"] = self.request.user.id
            return self.form_class(data=data)
        return self.form_class(**self.get_form_kwargs())

    def get_context_data(self, **kwargs):
        context = super(NewRequestPageView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        Request.objects.create(
            user=self.request.user,
            start_date=form.cleaned_data.get('start_date'),
            end_date=form.cleaned_data.get('end_date'),
            description=form.cleaned_data.get('description'),
            request_type=form.cleaned_data.get('request_type'),
            department=self.request.user.employee_department,
            status=Request.PENDING
        )
        Notification.objects.create(
            department=self.request.user.employee_department,
            message="User {} has made a new {} request".format(
                self.request.user, form.cleaned_data.get('request_type').name
            )
        )
        return super(NewRequestPageView, self).form_valid(form)
