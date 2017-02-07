from django.db import models


class Holiday(models.Model):
    name = models.CharField(max_length=150)
    date = models.DateField()

    def __unicode__(self):
        return self.name


class Calendar(models.Model):
    name = models.CharField(max_length=150)
    days = models.ManyToManyField(Holiday, blank=True)

    def __unicode__(self):
        return "{}-{}days".format(self.name, self.days.count())
