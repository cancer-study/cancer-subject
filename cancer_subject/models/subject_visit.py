from django.db import models

from edc_base.model_mixins import BaseUuidModel
from edc_base.model_managers import HistoricalRecords
from edc_consent.model_mixins import RequiresConsentMixin
from edc_metadata.model_mixins.creates import CreatesMetadataModelMixin
from edc_visit_tracking.constants import SCHEDULED
from edc_visit_tracking.managers import VisitModelManager
from edc_visit_tracking.model_mixins import (VisitModelMixin,
                                             PreviousVisitError)

from .appointment import Appointment


class SubjectVisit(VisitModelMixin, CreatesMetadataModelMixin,
                   RequiresConsentMixin, BaseUuidModel):

    """A model completed by the user that captures the covering
    information for the data collected for this timepoint/appointment,
    e.g.report_datetime.
    """

    appointment = models.OneToOneField(Appointment, on_delete=models.PROTECT)

    objects = VisitModelManager()

    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        self.info_source = 'subject'
        self.reason = SCHEDULED
        super().save(*args, **kwargs)

    @property
    def common_clean_exceptions(self):
        return super().common_clean_exceptions + [PreviousVisitError]

    class Meta(VisitModelMixin.Meta, RequiresConsentMixin.Meta):
        app_label = "cancer_subject"
        consent_model = 'cancer_subject.subjectconsent'
