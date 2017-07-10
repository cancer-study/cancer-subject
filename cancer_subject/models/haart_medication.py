from django.db import models

from edc.audit.audit_trail import AuditTrail

from .subject_base_uuid_model import SubjectBaseUuidModel
from .haart_record import HaartRecord
from ..choices.haart_record import MOD_REASON_CHOICE, ARV_REASON_CHOICE, HAART_MEDS_DRUG_NAMES
from ..managers import HaartMedRecordManager


class BaseHaartMedication(SubjectBaseUuidModel):

    drug_name = models.CharField(
        verbose_name="1.Drug Name",
        max_length=35,
        help_text="",
        choices=HAART_MEDS_DRUG_NAMES,
        )
    mod_reason = models.CharField(
        verbose_name="2.Mod Reason",
        max_length=65,
        null=True,
        blank=True,
        choices=MOD_REASON_CHOICE,
        )
    arv_reason = models.CharField(
        verbose_name="3.Reason for ARVs",
        max_length=25,
        choices=ARV_REASON_CHOICE,
        )
    start_date = models.DateField(
        verbose_name="4.Date Started",
        max_length=25,
        help_text="dd/mm/yyyy",
        )
    stop_date = models.DateField(
        verbose_name="5.Date Stopped",
        max_length=25,
        null=True,
        blank=True,
        help_text="dd/mm/yyyy",
        )

    class Meta:
        abstract = True


class HaartMedRecord(BaseHaartMedication):

    haart_record = models.ForeignKey(HaartRecord)

    objects = HaartMedRecordManager()

    history = AuditTrail()

    def natural_key(self):
        return (self.created, ) + self.haart_record.natural_key()

    def get_report_datetime(self):
        return self.haart_record.get_report_datetime()

    def get_subject_identifier(self):
        return self.haart_record.get_subject_identifier()

    def get_visit(self):
        return self.haart_record.subject_visit

    def __unicode__(self):
        return unicode(self.haart_record.subject_visit)

    class Meta:
        app_label = "cancer_subject"
        verbose_name = "Haart Medication"
