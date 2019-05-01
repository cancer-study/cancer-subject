# coding: utf-8
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from ..choices import CIGARETTE_SMOKING_CHOICE, SMOKE_NOW_CHOICE, WHEN_QUIT_CHOICE
from .model_mixins.crf_model_mixin import CrfModelMixin


class BaseRiskAssessmentSmoking (CrfModelMixin):

    smoke_now = models.CharField(
        verbose_name='Do you smoke cigarettes now?',
        max_length=35,
        choices=SMOKE_NOW_CHOICE,
    )

    cigarette_smoking = models.CharField(
        verbose_name='How many cigarettes do you smoke per day?',
        max_length=35,
        choices=CIGARETTE_SMOKING_CHOICE,
        null=True,
        blank=True,
    )

    years_smoked = models.IntegerField(
        verbose_name='For how many years have you smoked?',
        validators=[MinValueValidator(0), MaxValueValidator(90)],
        null=True,
        blank=True,
        help_text='If subject has quit smoking, leave blank.',
    )

    cigarette_smoked = models.CharField(
        verbose_name='How many cigarettes did you smoke per day?',
        max_length=35,
        choices=CIGARETTE_SMOKING_CHOICE,
        null=True,
        blank=True,
    )

    when_quit = models.CharField(
        verbose_name='When did you quit smoking cigarettes?',
        max_length=35,
        choices=WHEN_QUIT_CHOICE,
        null=True,
        blank=True,
    )

    years_smoked_before = models.IntegerField(
        verbose_name='For how many years did you smoke before quitting?',
        null=True,
        blank=True,
    )

    class Meta(CrfModelMixin.Meta):
        app_label = 'cancer_subject'
        verbose_name = 'Base Risk Assessment: Smoking'
        verbose_name_plural = 'Base Risk Assessment: Smoking'
