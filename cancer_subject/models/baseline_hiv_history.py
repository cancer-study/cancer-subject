from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.validators import RegexValidator
from django.db import models
from edc_base.model_validators.date import date_not_future
from edc_constants.choices import YES_NO, YES_NO_DONT_KNOW
from edc_reference.model_mixins import ReferenceModelMixin

from .model_mixins import CrfModelMixin


class BaselineHIVHistory (CrfModelMixin, ReferenceModelMixin):

    has_hiv_result = models.CharField(
        verbose_name=('Has the participant been previously '
                      'tested for HIV?'),
        max_length=25,
        choices=YES_NO_DONT_KNOW,
    )

    had_who_illnesses = models.CharField(
        verbose_name=('Has patient ever had any WHO stage 3 '
                      'or 4 illnesses?'),
        max_length=3,
        choices=YES_NO,
        help_text=('Refer to WHO classification document. DO NOT '
                   'include the current cancer diagnosis.'),)

    has_cd4 = models.CharField(
        verbose_name='Are \'CD4\' results available? ',
        max_length=3,
        choices=YES_NO,
    )

    # The following are added on this form from other forms on upgrade
    # LabResultCd4
    cd4_result = models.DecimalField(
        verbose_name=('What is the value of the most recent CD4 result'
                      ' (closest to time of cancer diagnosis)'),
        max_digits=6,
        null=True,
        blank=True,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(3000)],
        help_text='4-digit number field',)

    cd4_drawn_date = models.DateField(
        verbose_name='Date of recent CD4?',
        max_length=25,
        validators=[date_not_future],
        null=True,
        blank=True,
    )

    has_prior_cd4 = models.CharField(
        verbose_name='Is a CD4 result lower than the most recent '
        'CD4 result available?',
        max_length=3,
        choices=YES_NO,
    )

    nadir_cd4 = models.DecimalField(
        verbose_name=('What is the value of the lowest CD4 '
                      'result recorded'),
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(3000)],
        null=True,
        blank=True,
        help_text=('4-digit number field'),
    )

    nadir_cd4_drawn_date = models.DateField(
        verbose_name='Date of lowest CD4',
        max_length=25,
        validators=[date_not_future],
        null=True,
        blank=True,
    )

    # LabResultViralLoad
    has_vl = models.CharField(
        verbose_name='Are \'VIRAL LOAD\' results available? ',
        max_length=3,
        choices=YES_NO,
    )

    vl_result = models.CharField(
        verbose_name='HIV viral load result',
        max_length=25,
        null=True,
        blank=True,
        validators=[RegexValidator(
            r'^[<>=]{1}\d+$', 'Result must include \
            the quantifier (<, > or =) followed by \
            the numeric value',), ],
    )

    vl_drawn_date = models.DateField(
        verbose_name='Date of HIV viral load',
        max_length=25,
        validators=[date_not_future],
        null=True,
        blank=True,
    )

    class Meta(CrfModelMixin.Meta):
        app_label = 'cancer_subject'
        verbose_name = 'Baseline HIV History'
        verbose_name_plural = 'Baseline HIV History'
