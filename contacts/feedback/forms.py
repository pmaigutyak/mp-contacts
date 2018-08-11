
from django import forms

from captcha.fields import ReCaptchaField

from contacts.feedback.models import Feedback


class FeedbackForm(forms.ModelForm):

    captcha = ReCaptchaField()

    class Meta:
        model = Feedback
        fields = ['name', 'mobile', 'email', 'subject', 'text']
