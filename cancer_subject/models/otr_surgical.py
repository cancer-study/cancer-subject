from django.db import models
from edc_base.model_validators.date import datetime_not_future
from .model_mixins import CrfModelMixin


class OTRSurgical (CrfModelMixin):

    operation_performed = models.CharField(
        verbose_name='What operation was performed?: ',
        max_length=100,
    )

    date_operation = models.DateField(
        verbose_name='Date of operation?',
        max_length=15,
        blank=True,
        validators=[datetime_not_future],
        null=True,
    )

    class Meta(CrfModelMixin.Meta):
        app_label = 'cancer_subject'
        verbose_name = 'OTR: Surgical'
