from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.utils.translation import ugettext_lazy as _
from django.contrib.gis.db import models as geomodels
from providers.models import Provider


class ServiceArea(TimeStampedModel):
    name = models.CharField(verbose_name=_("Name"), max_length=128)
    poly = geomodels.PolygonField(verbose_name=_("Polygon"))
    price = geomodels.PositiveIntegerField(verbose_name=_("Price"))
    provider = models.ForeignKey(Provider, related_name='service_areas',
                                 on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = _('Service Area')
        verbose_name_plural = _('Service Areas')
        ordering = ('-created',)

