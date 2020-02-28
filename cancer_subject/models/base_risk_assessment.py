from django.db import models
from edc_base.model_validators import date_not_future
from edc_constants.choices import YES_NO_DONT_KNOW, YES_NO

from ..choices import AGE_FIRSTSEX_CHOICE, HEPATITIS_BEFORE_CHOICE
from ..choices import TRADMEDICINE_CHOICE, YES_NO_DECLINED
from .model_mixins.crf_model_mixin import CrfModelMixin


class BaseRiskAssessment (CrfModelMixin):

    hepatitis = models.CharField(
        verbose_name=('Have you been told you have hepatitis B or C '
                      'before?'),
        max_length=15,
        choices=HEPATITIS_BEFORE_CHOICE,
    )

    tuberculosis = models.CharField(
        verbose_name='Do you have now or have you ever had  tuberculosis?',
        max_length=25,
        choices=YES_NO_DONT_KNOW,
    )

    year_tb = models.CharField(
        verbose_name=('In what year did you last have tuberculosis '
                      '(year of diagnosis)?'),
        max_length=15,
        null=True,
        blank=True,
    )

    has_worked_mine = models.CharField(
        verbose_name='Have you ever worked at a mine?',
        max_length=35,
        choices=YES_NO_DECLINED,
    )

    has_smoked = models.CharField(
        verbose_name='Have you ever smoked cigarettes?',
        max_length=35,
        choices=YES_NO_DECLINED,
    )

    age_firstsex = models.CharField(
        verbose_name='How old were you when you first had sex?',
        max_length=35,
        choices=AGE_FIRSTSEX_CHOICE,
    )

    has_alcohol = models.CharField(
        verbose_name='Do you drink alcohol?',
        max_length=35,
        choices=YES_NO_DECLINED,
    )

    tradmedicine = models.CharField(
        verbose_name='How often do you use traditional medicine?',
        max_length=35,
        choices=TRADMEDICINE_CHOICE,
    )

    is_albino = models.CharField(
        verbose_name='Is patient an albino?',
        max_length=3,
        choices=YES_NO,
    )

    class Meta(CrfModelMixin.Meta):
        app_label = 'cancer_subject'
        verbose_name = 'Base Risk Assessment'
