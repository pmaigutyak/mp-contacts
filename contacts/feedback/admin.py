
from django.contrib import admin

from contacts.feedback.models import Feedback


class FeedbackAdmin(admin.ModelAdmin):

    list_display = [
        'subject', 'id', 'user', 'name', 'mobile', 'email', 'date_created'
    ]

    search_fields = ['name', 'subject', 'mobile', 'email', 'text']


admin.site.register(Feedback, FeedbackAdmin)
