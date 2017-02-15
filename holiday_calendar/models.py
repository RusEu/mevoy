from django.db import models


class Holiday(models.Model):
    """A free day that will not be calculated in an user request"""
    name = models.CharField(max_length=150)
    date = models.DateField()

    def __unicode__(self):
        return self.name


class Calendar(models.Model):
    """
    A calendar will includes a group of holidays.
    :param name: The name of the calendar. Ex: 'Holidays Madrid'.
    :param days: The holidays.
    """
    name = models.CharField(max_length=150)
    days = models.ManyToManyField(Holiday, blank=True)

    def __unicode__(self):
        return "{}-{}days".format(self.name, self.days.count())
