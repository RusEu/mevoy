import datetime

from django import forms
from django.utils.translation import ugettext as _

from auth_account.models import User

from vacation_request.models import RequestType


class RequestForm(forms.Form):
    error_messages = {
        "zero_days_left": _("You don't have days left for the type of request you chosen")
    }

    user = forms.ModelChoiceField(queryset=User.objects.all())
    start_date = forms.CharField(max_length=100, required=True)
    end_date = forms.CharField(max_length=100, required=True)
    description = forms.CharField(max_length=250, required=False)
    request_type = forms.ModelChoiceField(queryset=RequestType.objects.all())

    def clean_start_date(self):
        start_date = datetime.datetime.strptime(
            self.cleaned_data.get('start_date'), '%Y-%m-%dT%H:%M')
        return start_date

    def clean_end_date(self):
        end_date = datetime.datetime.strptime(
            self.cleaned_data.get('end_date'), '%Y-%m-%dT%H:%M')
        return end_date

    def clean(self):
        # If user does not have days left to make a request, raise error
        start_date = self.cleaned_data.get('start_date')
        end_date = self.cleaned_data.get('end_date')
        if start_date >= end_date:
            #raise error
            pass
        requested_days = (end_date - start_date).days
        request_type = self.cleaned_data.get('request_type')
        user = self.cleaned_data.get('user')
        days_left = user.days_left(request_type)["available_days"]
        if days_left == 0 or days_left < requested_days:
            raise forms.ValidationError(
                self.error_messages["zero_days_left"],
                code="zero_days_left"
            )
