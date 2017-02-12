from django.db import models

from django.utils.translation import ugettext_lazy as _


class RequestType(models.Model):
    PERIOD_TYPES = (
        ('week', _('Week')),
        ('month', _('Month')),
        ('year', _('Year')),
    )

    name = models.CharField(max_length=150)
    available_days = models.IntegerField(default=0)
    period = models.CharField(max_length=100, choices=PERIOD_TYPES)

    def __unicode__(self):
        return self.name


class Request(models.Model):
    APPROVED = "approved"
    DECLINED = "declined"
    PENDING = "pending"

    STATUS_TYPES = (
        (APPROVED, _('Approved')),
        (DECLINED, _('Declined')),
        (PENDING, _('Pending')),
    )

    user = models.ForeignKey('auth_account.User', related_name="user_requests")
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.TextField(blank=True, null=True)
    request_type = models.ForeignKey(RequestType)
    department = models.ForeignKey('company.Department')
    status = models.CharField(max_length=100,
                              choices=STATUS_TYPES,
                              default='pending')

    def __unicode__(self):
        return "{}, {}".format(self.user.email,
                               (self.end_date-self.start_date).days)


class Modificator(models.Model):
    SETTER = 'setter'
    CALCULATOR = 'calculator'

    MODIFICATOR_TYPES = (
        (SETTER, _('Setter')),
        (CALCULATOR, _('Calculator')),
    )

    name = models.CharField(max_length=150)
    request_type = models.ForeignKey(RequestType)
    days = models.IntegerField(default=0)
    modificator_type = models.CharField(max_length=100,
                                        choices=MODIFICATOR_TYPES)

    def __unicode__(self):
        return self.name
