from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.utils.translation import ugettext, ugettext_lazy as _
from django import forms

from company.models import Department


class LoginForm(AuthenticationForm):
    error_messages = {
        'department_incorrect': _('The provided department does not exist'),
        'department_not_allowed': _('You are not allowed to join this department')
    }

    department = forms.CharField(max_length=100)

    def clean_department(self):
        department = Department.objects.filter(
            id=self.cleaned_data.get('department')).first()
        if not department:
            raise forms.ValidationError(
                self.error_messages['department_incorrect'],
                code='department_incorrect'
            )
        return department

    def confirm_login_allowed(self, user):
        """
        Controls whether the given User may log in. This is a policy setting,
        independent of end-user authentication. This default behavior is to
        allow login by active users, and reject login by inactive users.

        If the given user cannot log in, this method should raise a
        ``forms.ValidationError``.

        If the given user may log in, this method should return None.
        """
        if not user.is_active:
            raise forms.ValidationError(
                self.error_messages['inactive'],
                code='inactive',
            )
        department = self.cleaned_data.get('department')

        user_is_employee = user in department.employees.all()
        user_is_manager = user in department.managers.all()
        if not any([user_is_employee, user_is_manager]):
            raise forms.ValidationError(
                self.error_messages['department_not_allowed'],
                code='department_not_allowed'
            )


class ProfileForm(forms.Form):
    pass
