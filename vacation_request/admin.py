from django.contrib import admin

from vacation_request.models import (Request,
                                     RequestType,
                                     Modificator)


class RequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'start_date', 'end_date', 'request_type')


class RequestTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'available_days')


class ModificatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'request_type', 'days', 'modificator_type')


admin.site.register(Request, RequestAdmin)
admin.site.register(RequestType, RequestTypeAdmin)
admin.site.register(Modificator, ModificatorAdmin)
