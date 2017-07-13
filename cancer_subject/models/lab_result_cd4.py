# coding: utf-8
from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator

from .model_mixins import CrfModelMixin


class LabResultCd4(CrfModelMixin):

    cd4_drawn_date = models.DateField(
        verbose_name="5. Date of CD4 cell count",
        max_length=25,
        help_text="",
    )

    cd4_result = models.DecimalField(
        verbose_name="6. CD4 cell count result",
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(3000)],
        help_text="",
    )

    class Meta(CrfModelMixin.Meta):
        app_label = "cancer_subject"
        verbose_name = "Lab Result: CD4"
        verbose_name_plural = "Lab Result: CD4"
