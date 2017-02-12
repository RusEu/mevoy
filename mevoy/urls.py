from django.contrib import admin
from django.contrib.auth.views import logout
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

from auth_account.views import LoginUserPageView


urlpatterns = [
    url(r'^login/$', LoginUserPageView.as_view(), name='login'),
    url(r'^logout/$', logout, {"next_page": "/login/"}),

    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('auth_account.urls')),
    url(r'^vacation_requests/', include('vacation_request.urls')),
    url(r'^calendar/', include('holiday_calendar.urls')),
    url(r'^notifications/', include('notifications.urls')),
    url('^', include('django.contrib.auth.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
