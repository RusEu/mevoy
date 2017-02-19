from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext as _
from django import forms

from company.models import Department

from auth_account.models import User


class LoginForm(AuthenticationForm):
    department = forms.CharField(max_length=100)
    login_as_manager = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.error_messages.update({
            'department_incorrect': _(
                'The provided department does not exist'),
            'department_user_not_allowed': _(
                'You are not allowed to join this department'),
            'department_user_not_manager': _(
                'You are not allowed to join the department as a manager')
        })

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

        if self.cleaned_data.get('login_as_manager', False):
            # Check if the current user is a manager of the department
            if user not in department.managers.all():
                raise forms.ValidationError(
                    self.error_messages['department_user_not_manager'],
                    code='department_user_not_manager'
                )
        else:
            if user not in department.employees.all():
                # Check if the user is an employee of the department
                raise forms.ValidationError(
                    self.error_messages["department_user_not_allowed"],
                    code="department_user_not_allowed"
                )


class ProfileForm(forms.ModelForm):
    """Form to modify the user's profile"""
    error_messages = {
        "email_not_unique": _("An account with the provided email already exists")
    }

    job_title = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control', "disabled": "disabled"}
        )
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'gender',
                  'profile_picture', 'job_title')
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'email': forms.EmailInput(
                attrs={'class': 'form-control'}
            ),
            'gender': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'profile_picture': forms.FileInput(
                attrs={'class': 'form-control'}
            )
        }

    def clean_job_title(self):
        # User cannot modify his job title
        return self.instance.job_title
