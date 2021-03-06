from django.views.generic.base import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from notifications.models import Notification


class NotificationsPageView(TemplateView):

    template_name = "notifications/index.html"

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(NotificationsPageView, self).dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(NotificationsPageView, self).get_context_data(*args,
                                                                      **kwargs)
        return context

    def post(self, request, *args, **kwargs):
        notifications_id = request.POST.getlist('notifications[]')
        # Not sure if we should let the managers delete notifications :/
        notifications = Notification.objects.filter(id__in=notifications_id)
        notifications.delete()
        return HttpResponse(status=200)
