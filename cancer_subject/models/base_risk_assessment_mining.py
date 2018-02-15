from django.db import models

from edc_base.model_fields.custom_fields import OtherCharField
from edc_constants.choices import YES_NO_DONT_KNOW

from ..choices import MINE_TYPE_CHOICE, TOTAL_TIME_CHOICE
from .model_mixins.crf_model_mixin import CrfModelMixin


class BaseRiskAssessmentMining (CrfModelMixin):

    mine_time = models.CharField(
        verbose_name=('What is the total amount of time you '
                      'worked in the mine?'),
        max_length=25,
        choices=TOTAL_TIME_CHOICE,
    )

    mine_type = models.CharField(
        verbose_name='What kind of mine have you worked in?',
        max_length=25,
        choices=MINE_TYPE_CHOICE,
    )

    mine_prompt_other = OtherCharField()

    mine_underground = models.CharField(
        verbose_name='Have you ever worked UNDERGROUND in a mine?',
        max_length=25,
        choices=YES_NO_DONT_KNOW,
    )

    mine_underground_time = models.CharField(
        verbose_name=('What is the total amount of time you '
                      'worked UNDERGROUND in the mine?'),
        max_length=25,
        choices=TOTAL_TIME_CHOICE,
        blank=True,
    )

    last_mine = models.DateField(
        verbose_name='When did you last work in a mine?',
        max_length=25,
    )

    class Meta:
        app_label = 'cancer_subject'
        verbose_name = 'Base Risk Assessment: Mining'
        verbose_name_plural = 'Base Risk Assessment: Mining'
        consent_model = 'cancer_subject.subjectconsent'
