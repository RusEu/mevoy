from django.conf.urls import url

from vacation_request.views import (NewRequestPageView,
                                    PendingRequestsPageView,
                                    ApprovedRequestsPageView,
                                    DeclinedRequestsPageView)


urlpatterns = [
    url(r'^new_request/$', NewRequestPageView.as_view(), name='new_request'),
    url(r'^pending_requests/(?P<section>\w+)/$',
        PendingRequestsPageView.as_view(),
        name='pending_requests'),
    url(r'^declined_requests/(?P<section>\w+)/$',
        DeclinedRequestsPageView.as_view(),
        name='declined_requests'),
    url(r'^approved_requests/(?P<section>\w+)/$',
        ApprovedRequestsPageView.as_view(),
        name='approved_requests'),
]
