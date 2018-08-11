
from django.apps import apps
from django.core.mail import mail_managers
from django.template.loader import render_to_string
from django.contrib.sites.models import Site


def send_notification(obj, subject_template, email_template, sms_template):

    context = {
        'object': obj,
        'site': Site.objects.get_current()
    }

    subject = render_to_string(subject_template, context)

    html = render_to_string(email_template, context)

    mail_managers(subject=subject.strip(), message='', html_message=html)

    if apps.is_installed('turbosms'):
        from turbosms.lib import send_sms_from_template
        send_sms_from_template(sms_template, context)
