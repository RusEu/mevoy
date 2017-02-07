import factory

from auth_account.factories import UserFactory

from . import models


class NotificationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Notification

    user = factory.SubFactory(UserFactory)
    name = factory.Faker('name')
    description = factory.Faker('description')
    notification_type = factory.Faker('notification_type')
