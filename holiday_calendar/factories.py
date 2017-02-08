import datetime
import factory

from . import models


class HolidayFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Holiday
        django_get_or_create = ('name',)

    name = factory.Faker('name')
    date = factory.LazyFunction(datetime.datetime.now)


class CalendarFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Calendar
        django_get_or_create = ('name',)

    name = factory.Faker('name')

    @factory.post_generation
    def days(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for holiday in extracted:
                self.days.add(holiday)
