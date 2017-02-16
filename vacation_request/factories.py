import datetime
import factory

from django.utils import timezone

from auth_account.factories import UserFactory
from company.factories import DepartmentFactory

from . import models


class RequestTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.RequestType
        django_get_or_create = ('name',)

    name = factory.Faker('name')
    available_days = 20


class RequestFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Request
        django_get_or_create = ('start_date', 'end_date',)

    user = factory.SubFactory(UserFactory)
    start_date = factory.LazyFunction(timezone.now)
    end_date = factory.LazyFunction(timezone.now)
    description = factory.Faker('name')
    department = factory.SubFactory(DepartmentFactory)
    request_type = factory.SubFactory(RequestTypeFactory)
    status = 'pending'


class ModificatorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Modificator
        django_get_or_create = ('name',)

    name = factory.Faker('name')
    request_type = factory.SubFactory(RequestTypeFactory)
    days = 10
    modificator_type = 'setter'
