from django.db import models
from django.utils.translation import ugettext_lazy as _


class Notification(models.Model):
    NOTIFICATION_TYPES = (
        ('success', _('Success')),
        ('warning', _('Warning')),
        ('error', _('Error')),
    )

    user = models.ForeignKey('auth_account.User', blank=True, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    notification_type = models.CharField(choices=NOTIFICATION_TYPES,
                                         max_length=100)

    def __unicode__(self):
        return self.name
