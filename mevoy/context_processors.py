from django.contrib.sites.shortcuts import get_current_site

from company.models import Department
from vacation_request.models import Request
from notifications.models import Notification


def global_processor(request):
    if request.user.is_anonymous():
        return {}

    notifications = Notification.objects.filter(user=request.user)

    context = {
        "SITE_NAME": get_current_site(request).name,
        "unknown_user_image": "http://www.wpclipart.com/signs_symbol/icons_oversized/male_user_icon.png",
        "notifications": notifications
    }

    # TODO: OPTIMIZE ME
    if request.session.get('is_employee'):
        employee_requests = Request.objects.filter(user=request.user)
        context.update(dict(
            employee_pending_requests=employee_requests.filter(status="pending"),
            employee_approved_requests=employee_requests.filter(status="approved"),
            employee_declined_requests=employee_requests.filter(status="declined")
        ))
    if request.session.get('is_manager'):
        department = Department.objects.get(name=request.session['department'])
        manager_requests = Request.objects.filter(department=department)
        context.update(dict(
            manager_pending_requests=manager_requests.filter(status="pending"),
            manager_approved_requests=manager_requests.filter(status="approved"),
            manager_declined_requests=manager_requests.filter(status="declined")
        ))

    return context
