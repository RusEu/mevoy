from django.conf.urls import url

from holiday_calendar.views import CalendarPageView, CalendarApiView

urlpatterns = [
    url(r'^api/$', CalendarApiView.as_view(), name='calendar_api'),
    url(r'^(?P<request_type>\d+)/$', CalendarPageView.as_view(), name='calendar'),
]
