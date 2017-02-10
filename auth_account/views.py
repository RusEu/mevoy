from django.views.generic.base import TemplateView
from django.views.generic import FormView
from django.core.urlresolvers import reverse
from django.contrib.auth import login
from django.http import HttpResponseRedirect

from company.models import Department

from auth_account.forms import LoginForm


class ProfilePageView(TemplateView):
    template_name = "auth_account/profile.html"

    def get_context_data(self, **kwargs):
        context = super(ProfilePageView, self).get_context_data(**kwargs)
        return context


class LoginUserPageView(FormView):
    template_name = "auth_account/login.html"
    form_class = LoginForm

    def get_context_data(self, **kwargs):
        context = super(LoginUserPageView, self).get_context_data(**kwargs)
        context["departments"] = Department.objects.all()
        return context

    def form_valid(self, form):
        login(self.request, form.get_user())
        department = form.cleaned_data["department"]
        self.request.session["department"] = department.name
        if self.request.user in department.employees.all():
            self.request.session["is_employee"] = True
            success_url = reverse('new_request')
        if self.request.user in department.managers.all():
            self.request.session["is_manager"] = True
            success_url = reverse('pending_requests',
                                  kwargs={"section": "manager"})
        return HttpResponseRedirect(success_url)
