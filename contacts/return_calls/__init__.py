
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ReturnCallsAppConfig(AppConfig):

    name = 'contacts.return_calls'
    verbose_name = _('ReturnCall')


default_app_config = 'contacts.return_calls.ReturnCallsAppConfig'
