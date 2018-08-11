
from datetime import time

from django.forms.widgets import Select


def get_time_choices(start, end):

    choices = []

    for i in range(start, end):

        for minutes in ['00', '30']:
            time = '{}:{}'.format(str(i).zfill(2), minutes)
            choices.append((time, time), )

    time = '{}:00'.format(str(end).zfill(2))
    choices.append((time, time), )

    return choices


class TimeSelect(Select):

    def __init__(self, attrs=None, start=8, end=22):
        super().__init__(attrs, choices=get_time_choices(start, end))

    def format_value(self, value):

        if isinstance(value, time):
            value = value.strftime('%H:%M')

        return super().format_value(value)
