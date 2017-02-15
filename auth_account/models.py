from django.db import models
from django.apps import apps
from django.utils import timezone
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import (AbstractBaseUser,
                                        PermissionsMixin)
from django.contrib.auth.models import Group as DjangoGroup, UserManager
from django.core.mail import send_mail


class Group(DjangoGroup):
    """
    A user group to define the request types that an employee can make and a
    holiday calendar that an user can have.
    Can also set the permissions that a user have to modify an model

    :param request_types: The request types a user can make.
    :param holiday_calendar: Calendar with all the holidays a user have.
    """
    request_types = models.ManyToManyField('vacation_request.RequestType',
                                           related_name="user_groups")
    holiday_calendar = models.ForeignKey('holiday_calendar.Calendar')

    def __unicode__(self):
        return self.name


class User(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = (
        ('male', _('Man')),
        ('female', _('Women')),
    )

    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(max_length=150, unique=True)
    gender = models.CharField(max_length=100,
                              choices=GENDER_CHOICES,
                              blank=True,
                              null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures',
                                        blank=True,
                                        null=True)
    job_title = models.ForeignKey('company.Job')
    modificators = models.ManyToManyField('vacation_request.Modificator',
                                          blank=True)
    groups = models.ManyToManyField(Group)

    is_staff = models.BooleanField('staff status', default=False)
    is_active = models.BooleanField('active', default=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name',
                       'job_title', 'department']

    objects = UserManager()

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @cached_property
    def request_types(self):
        """
        All the request types that a user can have
        """
        RequestType = apps.get_model('vacation_request.RequestType')
        return RequestType.objects.filter(
            user_groups__in=self.groups.all()
        ).distinct()

    def approved_requests(self, department):
        """
        Approved requests of the current user for an specific department
        :param department: The department where the request has been made.
        :type department: string
        """
        return self.user_requests.filter(department__name=department,
                                         status='approved')

    def pending_requests(self, department):
        """
        Pending requests of the current user for an specific department
        :param department: The department where the request has been made.
        :type department: string
        """
        return self.user_requests.filter(department__name=department,
                                         status="pending")

    def declined_requests(self, department):
        """
        Declined requests of the current user for an specific department
        :param department: The department where the request has been made.
        :type department: string
        """
        return self.user_requests.filter(department__name=department,
                                         status="declined")

    def __unicode__(self):
        return "{}, {}".format(self.first_name, self.last_name)
