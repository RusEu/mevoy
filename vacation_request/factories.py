import factory

from auth_account.factories import UserFactory

from . import models


class RequestTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Request

    name = factory.Faker('name')
    available_days = factory.Faker('available_days')


class RequestFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.RequestType

    user = factory.SubFactory(UserFactory)
    start_date = factory.Faker('start_date')
    end_date = factory.Faker('end_date')
    description = factory.Faker('description')
    request_type = factory.SubFactory(RequestTypeFactory)
    status = factory.Faker('status')

class ModificatorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Modificator

    name = factory.Faker('name')
    request_type = factory.SubFactory(RequestTypeFactory)
    days = factory.Faker('days')
    modificator_type = factory.Faker('modificator_type')
