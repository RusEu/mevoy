from django.contrib import admin

from auth_account.models import Group, User
from django.contrib.auth.models import Group as DjangoGroup


class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'holiday_calendar')


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name')


admin.site.register(User, UserAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.unregister(DjangoGroup)
