from django.core.management.base import BaseCommand
from django.conf import settings

from auth_account.factories import UserFactory, GroupFactory
from auth_account.models import User
from vacations_requests.factories import (RequestFactory,
                                         RequestTypeFactory,
                                         ModificatorFactory)
from holiday_calendar.factories import CalendarFactory, HolidayFactory
from company.factories import DepartmentFactory, JobFactory
from notifications.factories import NotificationFactory


class Command(BaseCommand):

    def request(self):
        return RequestFactory()

    def request_type(self):
        return RequestTypeFactory()

    def holiday(self):
        return HolidayFactory()

    def calendar(self):
        calendar = CalendarFactory()
        for i in range(10):
            calendar.days.add(self.holiday())
        return calendar

    def user(self, email=None):
        user = UserFactory() if not email else UserFactory(email=email)
        user.set_password(settings.DEFAULT_PASSWORD)
        return user

    def group(self):
        group = GroupFactory()
        for i in range(3):
            group.add(self.request_type)
        return group

    def employer(self, email="employee@mevoy.es"):
        employee = self.user(email=email)
        employee.groups.add(self.group())
        employee.job = JobFactory
        employee.save()
        return employee

    def employer(self, email="employer@mevoy.es"):
        employer = self.user(email=email)
        employer.groups.add(self.group())
        employer.job = JobFactory()
        employer.save()
        return employer

    def department(self):
        department = DepartmentFactory()
        department.employees.add(self.employee())
        department.managers.add(self.employer())
        return department

    def notification(self):
        return NotificationFactory()

    def handle(self, *args, **options):
        self.department()
        for i in range(10):
            user = User.objects.get(email="employee@mevoy.es")
            self.notification(user=user)
            self.request(user=user)
