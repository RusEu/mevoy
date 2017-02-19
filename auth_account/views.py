from django.views.generic.base import TemplateView
from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import login
from django.http import HttpResponseRedirect

from company.models import Department

from auth_account.models import User
from auth_account.forms import LoginForm, ProfileForm


class ProfilePageView(FormView):
    template_name = "auth_account/profile.html"
    form_class = ProfileForm
    success_url = reverse_lazy('profile')

    def get_form(self):
        try:
            return self.form_class(instance=self.request.user,
                                   **self.get_form_kwargs())
        except User.DoesNotExist:
            return self.form_class(**self.get_form_kwargs())

    def get_initial(self):
        initial = super(ProfilePageView, self).get_initial()
        initial["first_name"] = self.request.user.first_name
        initial["last_name"] = self.request.user.last_name
        initial["email"] = self.request.user.email
        initial["gender"] = self.request.user.gender
        initial["profile_picture"] = self.request.user.profile_picture
        initial["job_title"] = self.request.user.job_title.title
        return initial

    def get_context_data(self, **kwargs):
        context = super(ProfilePageView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.save()
        return super(ProfilePageView, self).form_valid(form)


class LoginUserPageView(FormView):
    template_name = "auth_account/login.html"
    form_class = LoginForm

    def form_valid(self, form):
        login(self.request, form.get_user())
        if form.cleaned_data.get('login_as_manager'):
            self.request.session["is_manager"] = True
            success_url = reverse_lazy("pending_requests")
        else:
            success_url = reverse_lazy("new_request")
        return HttpResponseRedirect(success_url)
