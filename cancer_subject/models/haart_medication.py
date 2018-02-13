from django.db import models
from edc_base.model_mixins import BaseUuidModel

from ..choices import MOD_REASON_CHOICE, ARV_REASON_CHOICE, HAART_MEDS_DRUG_NAMES
from .haart_record import HaartRecord


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
        help_text='dd/mm/yyyy',
    )

    stop_date = models.DateField(
        verbose_name='Date Stopped:',
        max_length=25,
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

    class Meta:
        app_label = 'cancer_subject'
        verbose_name = 'Haart Medication'
