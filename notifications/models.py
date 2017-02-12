from django.db import models


class Notification(models.Model):
    user = models.ForeignKey('auth_account.User', blank=True, null=True)
    department = models.ForeignKey('company.Department', blank=True, null=True)
    message = models.CharField(max_length=100)
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-datetime']

    def __unicode__(self):
        return self.name
