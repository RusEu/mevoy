import factory

from holiday_calendar.factories import CalendarFactory
from company.factories import JobFactory

from . import models


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.User
        django_get_or_create = ('username',)

    username = factory.Sequence(lambda n: "user_%d" % n)
    first_name = factory.Faker('name')
    last_name = factory.Faker('name')
    email = factory.LazyAttribute(lambda a: '{0}.{1}@example.com'.format(
        a.first_name, a.last_name).lower())
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
        django_get_or_create = ('name',)

    name = factory.Faker('name')
    holiday_calendar = factory.SubFactory(CalendarFactory)

    @factory.post_generation
    def request_types(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for request_type in extracted:
                self.request_types.add(request_type)
