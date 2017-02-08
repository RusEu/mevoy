from django.conf.urls import url

from notifications.views import NotificationsPageView

urlpatterns = [
    url(r'^$', NotificationsPageView.as_view(), name='notifications'),
]
