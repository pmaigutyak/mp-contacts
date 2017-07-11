
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ContactsAppConfig(AppConfig):
    name = 'contacts'
    verbose_name = _('Contacts')


default_app_config = 'contacts.ContactsAppConfig'

__version__ = '3.0'
