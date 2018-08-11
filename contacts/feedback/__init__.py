
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class FeedbackAppConfig(AppConfig):

    name = 'contacts.feedback'
    verbose_name = _('Feedback')


default_app_config = 'contacts.feedback.FeedbackAppConfig'
