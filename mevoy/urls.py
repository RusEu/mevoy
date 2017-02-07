from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('auth_account.urls')),
    url(r'^vacantion_requests/', include('vacation_request.urls')),
    url(r'^calendar/', include('holiday_calendar.urls')),
    url('^', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
