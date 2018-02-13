# coding: utf-8
from django.db import models

from .model_mixins import CrfModelMixin

from ..choices import TB_TREATMENT_CHOICE


class LabResultTb(CrfModelMixin):

    tb_description = models.CharField(
        verbose_name=('Describe tubercolosis diagnostic test results '
                      '(record test, date, result and units)'),
        max_length=65,
    )

    tb_treatment = models.CharField(
        verbose_name=('Is participant being treated for tuberculosis '
                      'now?'),
        max_length=50,
        choices=TB_TREATMENT_CHOICE,
    )

    tb_treatment_start = models.DateField(
        verbose_name=('When did the participant\'s treatment for '
                      'tuberculosis begin?'),
        max_length=25,
        null=True,
        blank=True,
    )

    class Meta(CrfModelMixin.Meta):
        app_label = 'cancer_subject'
        verbose_name = 'Lab Result: Tubercolosis'
        verbose_name_plural = 'Lab Result: Tubercolosis'
