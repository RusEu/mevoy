from django.conf.urls import url

from auth_account.views import ProfilePageView


urlpatterns = [
    url(r'^profile/$', ProfilePageView.as_view(), name='profile'),
]
