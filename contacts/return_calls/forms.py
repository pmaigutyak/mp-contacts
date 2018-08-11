
from django import forms

from captcha.fields import ReCaptchaField

from contacts.return_calls.models import ReturnCall
from contacts.return_calls.widgets import TimeSelect


class ReturnCallForm(forms.ModelForm):

    captcha = ReCaptchaField()

    class Meta:

        model = ReturnCall

        fields = [
            'answer_time', 'answer_start_time', 'answer_end_time', 'comment',
            'mobile'
        ]

        widgets = {
            'answer_time': forms.RadioSelect,
            'answer_start_time': TimeSelect,
            'answer_end_time': TimeSelect
        }
