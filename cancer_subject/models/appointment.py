from django.conf import settings
from django.contrib.sites.models import Site
from django.db import models
from edc_appointment.managers import AppointmentManager
from edc_appointment.model_mixins import AppointmentModelMixin
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import CurrentSiteManager as BaseCurrentSiteManager, SiteModelMixin


class CurrentSiteManager(BaseCurrentSiteManager):

    def get_queryset(self):
        try:
            REVIEWER_SITE_ID = settings.REVIEWER_SITE_ID
        except AttributeError:
            REVIEWER_SITE_ID = 0
        if int(settings.SITE_ID) == int(REVIEWER_SITE_ID):
            queryset = models.Manager.get_queryset(self)
        else:
            return super().get_queryset().filter(
                **{self._get_field_name() + '__id__in': settings.SITE_IDS})
        return queryset


class Appointment(AppointmentModelMixin, SiteModelMixin, BaseUuidModel):

    site = models.ForeignKey(
        Site, on_delete=models.PROTECT, null=True, editable=False,
        related_name='appointment_site')

    on_site = CurrentSiteManager()

    objects = AppointmentManager()

    history = HistoricalRecords()

    def natural_key(self):
        return (self.subject_identifier,
                self.visit_schedule_name,
                self.schedule_name,
                self.visit_code,
                self.visit_code_sequence)
    natural_key.dependencies = ['sites.Site']

    class Meta(AppointmentModelMixin.Meta):
        pass
