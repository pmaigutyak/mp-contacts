
from django.contrib import admin

from contacts.models import Feedback, ReturnCall


class FeedbackAdmin(admin.ModelAdmin):
    list_display = (
        'subject', 'id', 'user', 'name', 'mobile', 'email', 'date_created',
    )
    search_fields = ('name', 'subject', 'mobile', 'email', 'text', )


class ReturnCallAdmin(admin.ModelAdmin):
    list_display = (
        'mobile', 'id', 'get_answer_time_display', 'user', 'answer_start_time',
        'answer_end_time', 'date_created',
    )
    list_filter = ('answer_time',)
    search_fields = ('mobile', )


admin.site.register(ReturnCall, ReturnCallAdmin)

admin.site.register(Feedback, FeedbackAdmin)