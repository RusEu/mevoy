from django.db import models


class Department(models.Model):
    """
    Describes a company department and it includes all the employees
    and the managers of it.

    :param name: The name of the department.
    :param employees: All the employees that the department has.
    :param managers: All the managers that the department has.
    :param modificators: Modificators to modify a request type days left to the
                         entire department.

    """
    name = models.CharField(max_length=100, unique=True)
    employees = models.ManyToManyField('auth_account.User',
                                       related_name='employee_departments')
    managers = models.ManyToManyField('auth_account.User',
                                      related_name="manager_departments")
    modificators = models.ManyToManyField('vacation_request.Modificator',
                                          blank=True)

    def __unicode__(self):
        return self.name


class Job(models.Model):
    """
    Job title that an employee of a department can have

    :param title: Job title.
    :param description: Job description.
    :param modificators: Modificators to modify the days left for a request type
                         for all the employees that have this job.
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    modificators = models.ManyToManyField('vacation_request.Modificator',
                                          blank=True)

    def __unicode__(self):
        return self.title
