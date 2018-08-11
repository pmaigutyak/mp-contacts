
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model


class Feedback(models.Model):

    user = models.ForeignKey(
        get_user_model(), verbose_name=_('User'), blank=True,
        null=True, on_delete=models.SET_NULL)

    subject = models.CharField(_("Subject"), max_length=255)

    name = models.CharField(_("Name"), max_length=255)

    mobile = models.CharField(
        _("Mobile"), max_length=255, blank=True, null=True)

    email = models.EmailField(
        _("Email"), max_length=255, blank=True, null=True)

    date_created = models.DateTimeField(
        _('Date created'), auto_now_add=True, editable=False)

    text = models.TextField(_('Message text'), max_length=1000, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Feedback message')
        verbose_name_plural = _('Feedback messages')
