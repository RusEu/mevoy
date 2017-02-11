from django.conf.urls import url

from notifications.views import NotificationsPageView

urlpatterns = [
    url(r'^(?P<section>\w+)/$',
        NotificationsPageView.as_view(),
        name='notifications'),
]
