from django.contrib.sites.shortcuts import get_current_site

from vacation_request.models import Request
from notifications.models import Notification


def global_processor(request):
    if request.user.is_anonymous():
        return {}

    employee_pending_requests = Request.objects.filter(user=request.user,
                                                       status="pending")
    employee_approved_requests = Request.objects.filter(user=request.user,
                                                        status="approved")
    employee_declined_requests = Request.objects.filter(user=request.user,
                                                        status="declined")
    notifications = Notification.objects.filter(user=request.user)

    return {
        "SITE_NAME": get_current_site(request).name,
        "unknown_user_image": "http://www.wpclipart.com/signs_symbol/icons_oversized/male_user_icon.png",
        "employee_approved_requests": employee_approved_requests,
        "employee_declined_requests": employee_declined_requests,
        "employee_pending_requests": employee_pending_requests,
        "notifications": notifications
    }
