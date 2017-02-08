import factory

from . import models


class DepartmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Department
        django_get_or_create = ('name',)
    name = factory.Faker('name')

    @factory.post_generation
    def employees(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for employee in extracted:
                self.employees.add(employee)

    @factory.post_generation
    def managers(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for manager in extracted:
                self.managers.add(manager)

    @factory.post_generation
    def modificators(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for modificator in extracted:
                self.modificators.add(modificator)


class JobFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Job
        django_get_or_create = ('title',)
    title = factory.Faker('name')
    description = factory.Faker('name')

    @factory.post_generation
    def modificators(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for modificator in extracted:
                self.modificators.add(modificator)
