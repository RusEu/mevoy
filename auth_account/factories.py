import factory

from holiday_calendar.factories import CalendarFactory
from company.factories import JobFactory

from . import models


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.User

    username = factory.Sequence(lambda n: "user_%d" % n)
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    job_title = factory.SubFactory(JobFactory)
    gender = 'male'

    @factory.post_generation
    def modificators(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for modificator in extracted:
                self.modificators.add(modificator)

    @factory.post_generation
    def groups(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for group in extracted:
                self.groups.add(group)


class GroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Group

    holiday_calendar = factory.SubFactory(CalendarFactory)

    @factory.post_generation
    def request_types(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for request_type in extracted:
                self.request_types.add(request_type)
