from django.db import models
from edc_base.model_managers.historical_records import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators.date import date_not_future

from ..choices import HAART_MEDS_DRUG_NAMES
from ..choices import MOD_REASON_CHOICE, ARV_REASON_CHOICE
from .haart_record import HaartRecord


class ChemoMedRecordManager(models.Manager):

    def get_by_natural_key(self, drug_name, arv_reason, subject_identifier,
                           visit_schedule_name, schedule_name, visit_code):
        return self.get(
            drug_code=drug_name,
            dose_category=arv_reason,
            subject_visit__subject_identifier=subject_identifier,
            subject_visit__visit_schedule_name=visit_schedule_name,
            subject_visit__schedule_name=schedule_name,
            subject_visit__visit_code=visit_code)


class BaseHaartMedication(BaseUuidModel):

    drug_name = models.CharField(
        verbose_name='Drug Name:',
        choices=HAART_MEDS_DRUG_NAMES,
        max_length=35,
    )

    mod_reason = models.CharField(
        verbose_name='Mod Reason:',
        max_length=65,
        choices=MOD_REASON_CHOICE,
        null=True,
        blank=True,
    )

    arv_reason = models.CharField(
        verbose_name='Reason for ARVs:',
        max_length=25,
        choices=ARV_REASON_CHOICE,
    )

    start_date = models.DateField(
        verbose_name='Date Started:',
        max_length=25,
        validators=[date_not_future],
        help_text='dd/mm/yyyy',
    )

    stop_date = models.DateField(
        verbose_name='Date Stopped:',
        max_length=25,
        validators=[date_not_future],
        null=True,
        blank=True,
        help_text='dd/mm/yyyy',
    )

    class Meta:
        abstract = True


class HaartMedRecord(BaseHaartMedication):

    haart_record = models.ForeignKey(
        HaartRecord,
        on_delete=models.PROTECT)

    history = HistoricalRecords()

    def natural_key(self):
        return (self.drug_name, self.arv_reason) + self.haart_record.natural_key()
    natural_key.dependencies = ['cancer_subject.haart_record']

    class Meta:
        app_label = 'cancer_subject'
        verbose_name = 'Haart Medication'
