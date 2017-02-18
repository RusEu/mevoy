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

    department = request.session["department"]

    if request.session.get('is_manager'):
        requests = Request.objects.filter(department__name=department)
        request_types = RequestType.objects.filter(
            request__in=requests).distinct()
        context.update(dict(
            department_request_types=request_types,
            manager_pending_requests=requests.filter(status="pending"),
            manager_approved_requests=requests.filter(status="approved"),
            manager_declined_requests=requests.filter(status="declined"),
            manager_notification=Notification.objects.filter(
                department__name=department)
        ))
    else:
        employee = request.user
        context.update(dict(
            employee_pending_requests=employee.pending_requests(department),
            employee_approved_requests=employee.approved_requests(department),
            employee_declined_requests=employee.declined_requests(department)
        ))
    return context
