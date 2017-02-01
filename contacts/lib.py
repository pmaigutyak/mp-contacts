
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

    email_template = 'contacts/email/new_feedback_notification.html'

    context = {
        'feedback': feedback,
        'site': Site.objects.get_current()
    }

    html = render_to_string(email_template, context)

    mail_managers(subject=subject, message='', html_message=html)

    _send_sms('contacts/sms/new_feedback_notification.txt', context)


def send_new_return_call_notification(return_call):

    subject = _('New return call request #%s') % return_call.id

    email_template = 'contacts/email/new_return_call_notification.html'

    context = {
        'return_call': return_call,
        'site': Site.objects.get_current()
    }

    html = render_to_string(email_template, context)

    mail_managers(subject=subject, message='', html_message=html)

    _send_sms('contacts/sms/new_return_call_notification.txt', context)
