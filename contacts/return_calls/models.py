
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.conf import settings
from django.db import models


class ReturnCall(models.Model):

    ANSWER_TIME_FAST = 1
    ANSWER_TIME_FIXED = 2

    ANSWER_TIME_CHOICES = (
        (ANSWER_TIME_FAST, _('As fast as possible')),
        (ANSWER_TIME_FIXED, _('In fixed time')),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='return_calls',
        verbose_name=_('User'), blank=True, null=True,
        on_delete=models.SET_NULL)

    answer_time = models.PositiveIntegerField(
        _('Answer time'), null=False, choices=ANSWER_TIME_CHOICES,
        default=ANSWER_TIME_FAST)

    answer_start_time = models.TimeField(
        _('Start time'), blank=True, null=True, default='08:00')

    answer_end_time = models.TimeField(
        _('End time'), blank=True, null=True, default='08:30')

    mobile = models.CharField(_("Mobile"), max_length=21, blank=False)

    date_created = models.DateTimeField(
        _('Date created'), auto_now_add=True, editable=False)

    comment = models.TextField(_('Comment'), max_length=1000, blank=True)

    def clean_fields(self, exclude=None):

        if self.answer_time != self.ANSWER_TIME_FIXED:
            self.answer_start_time = None
            self.answer_end_time = None
            return

        errors = {}

        start_time = self.answer_start_time
        end_time = self.answer_end_time

        if not start_time:
            errors['answer_start_time'] = start_time.error_messages['required']

        if not end_time:
            errors['answer_end_time'] = end_time.error_messages['required']

        if errors:
            raise ValidationError(errors)

    @property
    def is_time_fixed(self):
        return self.answer_time == self.ANSWER_TIME_FIXED

    def __str__(self):
        return self.mobile

    class Meta:
        verbose_name = _('Return call')
        verbose_name_plural = _('Return calls')
