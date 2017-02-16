from django.db import models


class Department(models.Model):
    """
    Describes a company department and it includes all the employees
    and the managers of it.

    :param name: The name of the department.
    :param employees: All the employees that the department has.
    :param managers: All the managers that the department has.

    """
    name = models.CharField(max_length=100, unique=True)
    employees = models.ManyToManyField('auth_account.User',
                                       related_name='employee_departments')
    managers = models.ManyToManyField('auth_account.User',
                                      related_name="manager_departments")

    def __unicode__(self):
        return self.name


class Job(models.Model):
    """
    Job title that an employee of a department can have

    :param title: Job title.
    :param description: Job description.
    """
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return self.title
