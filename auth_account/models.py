from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import (AbstractBaseUser,
                                        PermissionsMixin)
from django.contrib.auth.models import Group as DjangoGroup, UserManager
from django.core.mail import send_mail


class Group(DjangoGroup):
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


    def __unicode__(self):
        return "{}, {}".format(self.first_name, self.last_name)
