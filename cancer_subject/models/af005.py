# coding: utf-8
from django.db import models

from .model_mixins import CrfModelMixin
from ..choices import DEATH_CAUSE_CATEGORY_CHOICE, PRIMARY_DEATH_CAUSE_CHOICE


class Af005 (CrfModelMixin):

    death_date = models.DateTimeField(
        verbose_name='Date of Death:',
        max_length=25,
        help_text='dd/mm/yyyy',
    )

    primary_death_cause = models.CharField(
        verbose_name='What is the primary source of cause of death '
        'information?',
        max_length=65,
        choices=PRIMARY_DEATH_CAUSE_CHOICE,
    )

    death_cause_description = models.CharField(
        verbose_name='Describe the primary cause of death.:',
        max_length=35,
    )

    death_cause_category = models.CharField(
        verbose_name='Based on the above description, what category '
        'best defines the primary cause of death?',
        max_length=85,
        choices=DEATH_CAUSE_CATEGORY_CHOICE,
    )

    diagnosis_code = models.CharField(
        verbose_name='Diagnosis code for primary cause of death:',
        max_length=8,
    )

    comments = models.CharField(
        verbose_name='Comments:',
        max_length=35,
    )

    class Meta(CrfModelMixin.Meta):
        app_label = 'cancer'
        verbose_name = 'AF005 Death Record'
