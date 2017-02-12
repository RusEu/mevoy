from django.contrib.sites.shortcuts import get_current_site

from vacation_request.models import Request, RequestType
from notifications.models import Notification


def global_processor(request):
    if request.user.is_anonymous():
        return {}

    notifications = request.user.notification_set.all().order_by('-datetime')
    context = {
        "SITE_NAME": get_current_site(request).name,
        "unknown_user_image": "http://www.wpclipart.com/signs_symbol/icons_oversized/male_user_icon.png",
        "employee_notifications": notifications
    }

    department = request.session["department"]
    requests = Request.objects.filter(department__name=department)

    # TODO: OPTIMIZE ME
    if request.session.get('is_employee'):
        employee_requests = requests.filter(user=request.user)
        context.update(dict(
            employee_pending_requests=employee_requests.filter(status="pending"),
            employee_approved_requests=employee_requests.filter(status="approved"),
            employee_declined_requests=employee_requests.filter(status="declined")
        ))
    if request.session.get('is_manager'):
        context.update(dict(
            manager_pending_requests=requests.filter(status="pending"),
            manager_approved_requests=requests.filter(status="approved"),
            manager_declined_requests=requests.filter(status="declined"),
            manager_notification=notifications.filter(department__name=department)
        ))

    return context
