from django.db import models

from django.utils.translation import ugettext_lazy as _


class RequestType(models.Model):
    """
    The request type that a user can make.
    :param name: The name of the request_types
    :param available_days: How many free days can an employee enjoy of this
                           request type.
    :param period: Describes the period for the available_days(week/month/year)
    :param approvals: How many managers should approve the request.
    """
    PERIOD_TYPES = (
        ('week', _('Week')),
        ('month', _('Month')),
        ('year', _('Year')),
    )

    name = models.CharField(max_length=150)
    available_days = models.IntegerField(default=0)
    period = models.CharField(max_length=100, choices=PERIOD_TYPES)
    approvals = models.IntegerField(default=1)

    def __unicode__(self):
        return self.name


class Request(models.Model):
    """
    The request that a user makes to receive free working days.
    :param user: The user that makes the request.
    :param start_date: The date when the user vacations will start.
    :param end_date: The date when the user vacations will end.
    :param description: The reason why a user is requesting a vacations.
    :param request_type: The type of the request
    :param department: The department that will receive the request and will
                       approve/decline it.
    :param status: The status that a request can have(pending/approved/declined)
    :param approvals: How many managers have approved the request
    """
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
    approvals = models.IntegerField(default=0)

    def __unicode__(self):
        return "{}, {}".format(self.user.email,
                               (self.end_date-self.start_date).days)


class Modificator(models.Model):
    """
    A modificator is used to modify a user free days for a request type.
    :param name: The name of the modificator.
    :param request_type: The available_days of the request type that should
                         modify.
    :param days: The days that will modify.
    :param modificator_type: The type of the modificator.
                             If the modificator is a setter, will set the days
                             that a user can request.
                             If the modificator is a calculator will add or
                             substract the number of days that a user can
                             request.
    """
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
