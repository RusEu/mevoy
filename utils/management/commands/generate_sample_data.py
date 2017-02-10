from django.core.management.base import BaseCommand
from django.conf import settings

from auth_account.factories import UserFactory, GroupFactory
from auth_account.models import User, Group
from vacation_request.factories import (ModificatorFactory,
                                        RequestFactory,
                                        RequestTypeFactory)
from holiday_calendar.factories import CalendarFactory, HolidayFactory
from company.factories import DepartmentFactory, JobFactory
from company.models import Department
from notifications.factories import NotificationFactory


class Command(BaseCommand):

    def modificator(self):
        return ModificatorFactory()

    def holiday(self):
        return HolidayFactory()

    def calendar(self):
        calendar = CalendarFactory.create(
            days=(HolidayFactory for HolidayFactory in range(10))
        )
        return calendar

    def user(self, username=None):
        request_types = (RequestTypeFactory for RequestTypeFactory in range(5))
        group = GroupFactory()
        for request_type in request_types:
            group.request_types.add(request_type)
        modificators = (ModificatorFactory for ModificatorFactory in range(5))
        if username:
            user = UserFactory(
                username=username,
                modificators=modificators)
            user.groups.add(group)
        else:
            user = UserFactory(modificators=modificators)
            user.groups.add(group)
        user.set_password(settings.DEFAULT_PASSWORD)
        user.save()
        return user

    def employee(self, username="employee"):
        employee = self.user(username=username)
        return employee

    def manager(self, username="manager"):
        manager = self.user(username=username)
        return manager

    def department(self):
        department = DepartmentFactory()
        department.employees.add(self.employee())
        department.managers.add(self.manager())
        return department

    def handle(self, *args, **options):
        Department.objects.all().delete()
        for i in range(3):
            self.department()
        for i in range(10):
            employee = User.objects.get(username="employee")
            manager = User.objects.get(username="manager")
            NotificationFactory(user=employee)
            NotificationFactory(user=manager)
        for i in range(10):
            RequestFactory(user=employee, status="approved")
            RequestFactory(user=employee, status="declined")
            RequestFactory(user=employee, status="pending")
