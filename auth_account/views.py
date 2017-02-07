from django.shortcuts import render
from django.views.generic.base import TemplateView


class ProfilePageView(TemplateView):
    template_name = "auth_account/profile.html"

    def get_context_data(self, **kwargs):
        context = super(ProfilePageView, self).get_context_data(**kwargs)
        return context
