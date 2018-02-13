from django.db import models

from .model_mixins import CrfModelMixin


class OTRSurgical (CrfModelMixin):

    operation_performed = models.CharField(
        verbose_name="What operation was performed?: ",
        max_length=100,
    )

    date_operation = models.DateField(
        verbose_name="Date of operation?",
        max_length=15,
        blank=True,
        null=True,
    )

    class Meta(CrfModelMixin.Meta):
        app_label = "cancer_subject"
        verbose_name = "OTR: Surgical"
