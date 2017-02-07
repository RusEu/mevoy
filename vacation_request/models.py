from django.db import models

from django.utils.translation import ugettext_lazy as _


class RequestType(models.Model):
    name = models.CharField(max_length=150)
    available_days = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name


class Request(models.Model):
    STATUS_TYPES = (
        ('approved', _('Approved')),
        ('declined', _('Declined')),
        ('pending', _('Pending')),
    )

    user = models.ForeignKey('auth_account.User', related_name="user_requests")
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.TextField(blank=True, null=True)
    request_type = models.ForeignKey(RequestType)
    status = models.CharField(max_length=100,
                              choices=STATUS_TYPES,
                              default='pending')

    def __unicode__(self):
        return "{}, {}".format(self.user.email,
                               (self.end_date-self.start_date).days)


class Modificator(models.Model):
    MODIFICATOR_TYPES = (
        ('setter', _('Setter')),
        ('calculator', _('Calculator')),
    )

    name = models.CharField(max_length=150)
    request_type = models.ForeignKey(RequestType)
    days = models.IntegerField(default=0)
    modificator_type = models.CharField(max_length=100,
                                        choices=MODIFICATOR_TYPES)

    def __unicode__(self):
        return self.name
