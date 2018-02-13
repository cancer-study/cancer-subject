# coding: utf-8
from django.db import models
from django.core.validators import RegexValidator

from .model_mixins import CrfModelMixin


class LabResultViralload(CrfModelMixin):

    vl_drawn_date = models.DateField(
        verbose_name='8. Date of HIV viral load',
        max_length=25,
    )

    vl_result = models.CharField(
        verbose_name='9. HIV viral load result',
        max_length=25,
        validators=[RegexValidator(r'^[<>=]{1}\d+$', 'Result must include \
                                   the quantifier (<, > or =) followed by \
                                   the numeric value',), ],
    )

    class Meta(CrfModelMixin.Meta):
        app_label = 'cancer_subject'
        verbose_name = 'Lab Result: Viral Load'
        verbose_name_plural = 'Lab Result: Viral Load'
