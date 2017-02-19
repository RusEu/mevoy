from django.db import models


class Notification(models.Model):
    """
    A notification that a user or a department can receive when a request is
    made by the employee or approved/rejected by the department manager .
    :param user: If the field is set, the notification is received by the user
    :param department: If the field is set, the notification is received by the
                       department.
    :param message: The massage that a user/department has to receive.
    :param datetime: Describes the date when the notification has been created.
    """
    user = models.ForeignKey('auth_account.User', blank=True, null=True)
    department = models.ForeignKey('company.Department', blank=True, null=True)
    message = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-creation_date']

    def __unicode__(self):
        return self.name
