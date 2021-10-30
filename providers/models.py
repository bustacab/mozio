from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
import uuid


class Provider(TimeStampedModel):
    """
        Model that represents a Provider.
        A provider should contain the following information:
        - Name
        - Email
        - Phone Number
        - Language
        - Currency
    """
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=128, verbose_name=_("Name"))
    email = models.EmailField(verbose_name=_("Email"))
    phone_number = PhoneNumberField(verbose_name=_("Phone Number"))
    language = models.CharField(max_length=128, verbose_name=_("Language"))
    currency = models.CharField(max_length=128, verbose_name=_("Currency"))

    class Meta:
        verbose_name = _('Provider')
        verbose_name_plural = _('Providers')
        ordering = ('-created',)
