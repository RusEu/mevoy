from django.conf.urls import url

from holiday_calendar.views import CalendarPageView

urlpatterns = [
    url(r'^(?P<section>\w+)/(?P<request_type>\d+)/$',
        CalendarPageView.as_view(),
        name='calendar'),
]
