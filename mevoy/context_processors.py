from django.contrib.sites.shortcuts import get_current_site


def site(request):
    site_name = get_current_site(request)
    return {"SITE_NAME": site_name.name}
