from django.conf.urls import url

from holiday_calendar.views import CalendarPageView

urlpatterns = [
    url(r'^$', CalendarPageView.as_view(), name='calendar'),
]
