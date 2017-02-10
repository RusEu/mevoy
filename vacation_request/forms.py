from django import forms

from vacation_request.models import Request


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['user', 'start_date', 'end_date', 'description',
                  'request_type', 'status']
