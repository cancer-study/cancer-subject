from django.db import models
from edc_appointment.models import Appointment
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin
from edc_consent.model_mixins import RequiresConsentFieldsModelMixin
from edc_constants.constants import NOT_APPLICABLE
from edc_metadata.model_mixins.creates import CreatesMetadataModelMixin
from edc_reference.model_mixins import ReferenceModelMixin
from edc_visit_tracking.constants import SCHEDULED
from edc_visit_tracking.managers import VisitModelManager
from edc_visit_tracking.model_mixins import (VisitModelMixin)

from ..choices import INFO_SOURCE, REASONS_MISSED_OR_DELAYED
from ..choices import VISIT_REASON, VISIT_UNSCHEDULED_REASON
from edc_visit_tracking.choices import VISIT_INFO_SOURCE
from edc_model_fields.fields.other_charfield import OtherCharField


# from .appointment import Appointment
class SubjectVisit(VisitModelMixin, ReferenceModelMixin,
                   CreatesMetadataModelMixin, SiteModelMixin,
                   RequiresConsentFieldsModelMixin, BaseUuidModel):

    """A model completed by the user that captures the covering
    information for the data collected for this timepoint/appointment,
    e.g.report_datetime.
    """

    appointment = models.OneToOneField(Appointment, on_delete=models.PROTECT)

    reason = models.CharField(
        verbose_name='What is the reason for this visit report?',
        max_length=25,
        choices=VISIT_REASON)

    reason_unscheduled = models.CharField(
        verbose_name=(
            'If \'Unscheduled\' above, provide reason for '
            'the unscheduled visit'),
        max_length=25,
        choices=VISIT_UNSCHEDULED_REASON,
        default=NOT_APPLICABLE)

    reason_missed = models.CharField(
        verbose_name='What is the reason for missing this visit?',
        max_length=25,
        choices=REASONS_MISSED_OR_DELAYED)

    info_source = models.CharField(
        verbose_name='What is the main source of this information?',
        max_length=25,
        choices=INFO_SOURCE)

    reason = models.CharField(
        verbose_name='What is the reason for this visit report?',
        max_length=25,
        choices=VISIT_REASON)

    reason_unscheduled = models.CharField(
        verbose_name=(
            'If \'Unscheduled\' above, provide reason for '
            'the unscheduled visit'),
        max_length=25,
        choices=VISIT_UNSCHEDULED_REASON,
        default=NOT_APPLICABLE)

    reason_missed = models.CharField(
        verbose_name='If \'Missed\' above, provide the reason the scheduled visit was missed',
        max_length=35,
        choices=VISIT_REASON,
        blank=True,
        null=True)

    info_source = models.CharField(
        verbose_name='What is the main source of this information?',
        max_length=25,
        choices=VISIT_INFO_SOURCE)

    info_source_other = OtherCharField(
        verbose_name='Other, specify',
        max_length=25,
    )

    objects = VisitModelManager()

    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        self.info_source = 'subject'
        self.reason = SCHEDULED
        super().save(*args, **kwargs)

    @property
    def common_clean_exceptions(self):
        return super().common_clean_exceptions  # + [PreviousVisitError]

    class Meta(VisitModelMixin.Meta, RequiresConsentFieldsModelMixin.Meta):
        app_label = "cancer_subject"
        consent_model = 'cancer_subject.subjectconsent'
