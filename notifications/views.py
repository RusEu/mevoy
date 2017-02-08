from django.shortcuts import render
from django.views.generic.base import TemplateView


class NotificationsPageView(TemplateView):

    template_name = "notifications/index.html"
