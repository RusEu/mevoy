from django.core.management.base import BaseCommand
from django.conf import settings

from auth_account.factories import UserFactory, GroupFactory
from vacation_request.factories import (RequestFactory,
                                        RequestTypeFactory)
from company.factories import DepartmentFactory, JobFactory
from notifications.factories import NotificationFactory


class Command(BaseCommand):

    def user(self, username, job_title, group):
        job = JobFactory(title=job_title)
        user = UserFactory(username=username, job_title=job)
        user.groups.add(group)
        user.set_password(settings.DEFAULT_PASSWORD)
        user.save()
        return user

    def department(self, department_name, employee, manager):
        department = DepartmentFactory(name=department_name)
        department.employees.add(employee)
        department.managers.add(manager)
        department.save()
        return department

    def create_department_IT(self):
        group = GroupFactory()
        for i in range(5):
            group.request_types.add(RequestTypeFactory())
        employee = self.user(username="developer",
                             job_title="Developer",
                             group=group)
        manager = self.user(username="cto",
                            job_title="CTO",
                            group=group)
        department = self.department("IT", employee, manager)

        for request_type in group.request_types.all():
            RequestFactory(user=employee,
                           department=department,
                           status='pending',
                           request_type=request_type)
            RequestFactory(user=employee,
                           department=department,
                           status='approved',
                           request_type=request_type)
            RequestFactory(user=employee,
                           department=department,
                           status='declined',
                           request_type=request_type)
        for i in range(5):
            NotificationFactory(user=employee)

    def create_department_SALES(self):
        group = GroupFactory()
        for i in range(5):
            group.request_types.add(RequestTypeFactory())
        employee = self.user(username="commercial",
                             group=group,
                             job_title="commercial")
        manager = self.user(username="sales_manager",
                            group=group,
                            job_title="sales manager")
        department = self.department("SALES", employee, manager)
        for request_type in group.request_types.all():
            RequestFactory(user=employee,
                           request_type=request_type,
                           department=department,
                           status='pending')
            RequestFactory(user=employee,
                           request_type=request_type,
                           department=department,
                           status='approved')
            RequestFactory(user=employee,
                           request_type=request_type,
                           department=department,
                           status='declined')
        for i in range(5):
            NotificationFactory(user=employee)

    def create_department_PRODUCTION(self):
        group = GroupFactory()
        for i in range(5):
            group.request_types.add(RequestTypeFactory())
        employee = self.user(username="product_manager",
                             group=group,
                             job_title="product manager")
        manager = employee
        department = self.department("PRODUCT", employee, manager)
        for request_type in group.request_types.all():
            RequestFactory(user=employee,
                           request_type=request_type,
                           department=department,
                           status='pending')
            RequestFactory(user=employee,
                           request_type=request_type,
                           department=department,
                           status='approved')
            RequestFactory(user=employee,
                           request_type=request_type,
                           department=department,
                           status='declined')
        for i in range(5):
            NotificationFactory(user=employee)

    def handle(self, *args, **options):
        self.create_department_IT()
        self.create_department_SALES()
        self.create_department_PRODUCTION()
