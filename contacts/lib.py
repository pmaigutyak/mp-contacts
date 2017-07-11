
from django.apps import apps
from django.core.mail import mail_managers
from django.utils.translation import ugettext_lazy as _
from django.template.loader import render_to_string
from django.contrib.sites.models import Site


def _send_sms(template, context):
    if apps.is_installed('turbosms'):
        from turbosms.lib import send_sms_from_template
        send_sms_from_template(template, context)


def send_new_feedback_notification(feedback):

    subject = _('New feedback message #%s') % feedback.id

    email_template = 'contacts/feedback/email.html'

    context = {
        'feedback': feedback,
        'site': Site.objects.get_current()
    }

    html = render_to_string(email_template, context)

    mail_managers(subject=subject, message='', html_message=html)

    _send_sms('contacts/feedback/sms.txt', context)


def send_new_error_message_notification(error_message):

    subject = _('New error message #%s') % error_message.id

    email_template = 'contacts/error_message/email.html'

    context = {
        'error_message': error_message,
        'site': Site.objects.get_current()
    }

    html = render_to_string(email_template, context)

    mail_managers(subject=subject, message='', html_message=html)

    _send_sms('contacts/error_message/sms.txt', context)


def send_new_return_call_notification(return_call):

    subject = _('New return call request #%s') % return_call.id

    email_template = 'contacts/return_call/email.html'

    context = {
        'return_call': return_call,
        'site': Site.objects.get_current()
    }

    html = render_to_string(email_template, context)

    mail_managers(subject=subject, message='', html_message=html)

    _send_sms('contacts/return_call/sms.txt', context)
