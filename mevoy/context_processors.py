from django.contrib.sites.shortcuts import get_current_site

from vacation_request.models import Request, RequestType
from notifications.models import Notification


def global_processor(request):
    if request.user.is_anonymous():
        return {}

    context = {
        "SITE_NAME": get_current_site(request).name,
        "unknown_user_image": "http://www.wpclipart.com/signs_symbol/icons_oversized/male_user_icon.png",
    }

    if request.session.get('is_manager'):
        manager_departments = request.user.manager_departments.all()
        requests = Request.objects.filter(department__in=manager_departments)
        request_types = RequestType.objects.filter(
            request__in=requests).distinct()
        context.update(dict(
            request_types=request_types,
            manager_pending_requests=requests.filter(status="pending"),
            manager_approved_requests=requests.filter(status="approved"),
            manager_declined_requests=requests.filter(status="declined"),
            manager_notifications=Notification.objects.filter(
                department__in=manager_departments)
        ))
    return context
