import factory

from . import models


class HolidayFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Holiday

    name = factory.Faker('name')
    date = factory.Faker('date')


class CalendarFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Calendar

    name = factory.Faker('name')

    @factory.post_generation
    def days(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for holiday in extracted:
                self.days.add(holiday)
