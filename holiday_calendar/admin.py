from django.contrib import admin

from holiday_calendar.models import Holiday, Calendar


class CalendarAdmin(admin.ModelAdmin):
    list_display = ('name',)


class HolidayAdmin(admin.ModelAdmin):
    list_display = ('name', 'date',)


admin.site.register(Calendar, CalendarAdmin)
admin.site.register(Holiday, HolidayAdmin)
