from django.contrib.sites.shortcuts import get_current_site

from vacation_request.models import Request
from notifications.models import Notification


def global_processor(request):
    if request.user.is_anonymous():
        return {}

    pending_requests = Request.objects.filter(user=request.user,
                                              status="pending")
    approved_requests = Request.objects.filter(user=request.user,
                                               status="approved")
    declined_requests = Request.objects.filter(user=request.user,
                                               status="declined")
    notifications = Notification.objects.filter(user=request.user)

    return {
        "SITE_NAME": get_current_site(request).name,
        "unknown_user_image": "http://www.wpclipart.com/signs_symbol/icons_oversized/male_user_icon.png",
        "approved_requests": approved_requests,
        "declined_requests": declined_requests,
        "pending_requests": pending_requests,
        "notifications": notifications
    }
