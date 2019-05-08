from django.contrib.sites.managers import CurrentSiteManager
from django.core.exceptions import ValidationError
from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_identifier.managers import SubjectIdentifierManager
from edc_visit_schedule.model_mixins import OnScheduleModelMixin

from .subject_consent import SubjectConsent


class OnSchedule(OnScheduleModelMixin, BaseUuidModel):

    """A model used by the system. Auto-completed by subject_consent.
    """

    def save(self, *args, **kwargs):
        self.consent_version = self.get_consent_version()
        super(OnSchedule, self).save(*args, **kwargs)

    def get_consent_version(self):
        try:
            subject_consent_obj = SubjectConsent.objects.get(
                subject_identifier=self.subject_identifier)
        except SubjectConsent.DoesNotExist:
            raise ValidationError(
                'Missing Consent form. Cannot proceed.')
        else:
            return subject_consent_obj.version

    objects = SubjectIdentifierManager()

    history = HistoricalRecords()

    on_site = CurrentSiteManager()
