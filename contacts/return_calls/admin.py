
from django.db import models
from django.contrib import admin

from contacts.return_calls.models import ReturnCall
from contacts.return_calls.widgets import TimeSelect


class ReturnCallAdmin(admin.ModelAdmin):

    list_display = [
        'mobile', 'id', 'get_answer_time_display', 'user', 'answer_start_time',
        'answer_end_time', 'date_created'
    ]

    list_filter = ['answer_time']

    search_fields = ['mobile']

    formfield_overrides = {
        models.TimeField: {'widget': TimeSelect}
    }


admin.site.register(ReturnCall, ReturnCallAdmin)
