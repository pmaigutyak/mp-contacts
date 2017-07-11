
from django import forms

from captcha.fields import ReCaptchaField

from contacts.models import Feedback, ReturnCall, ErrorMessage


class FeedbackForm(forms.ModelForm):

    captcha = ReCaptchaField()

    class Meta:
        model = Feedback
        fields = ('name', 'mobile', 'email', 'subject', 'text', )


class ReturnCallForm(forms.ModelForm):

    class Meta:
        model = ReturnCall
        fields = (
            'answer_time', 'answer_start_time', 'answer_end_time', 'comment',
            'mobile',
        )
        widgets = {
            'answer_time': forms.RadioSelect
        }


class ErrorMessageForm(forms.ModelForm):

    captcha = ReCaptchaField()

    class Meta:
        model = ErrorMessage
        fields = ('text', 'name', 'email', 'mobile', )
