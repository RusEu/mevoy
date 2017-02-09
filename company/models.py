from django.db import models


class Department(models.Model):

    name = models.CharField(max_length=100)
    employees = models.ManyToManyField('auth_account.User',
                                       related_name='employee_departments')
    managers = models.ManyToManyField('auth_account.User',
                                      related_name="manager_departments")
    modificators = models.ManyToManyField('vacation_request.Modificator',
                                          blank=True)
    def __unicode__(self):
        return self.name


class Job(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    modificators = models.ManyToManyField('vacation_request.Modificator',
                                          blank=True)

    def __unicode__(self):
        return self.title
