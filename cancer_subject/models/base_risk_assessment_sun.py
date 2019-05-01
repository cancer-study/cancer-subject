from django.db import models

from ..choices import HOURS_OUTDOOR_CHOICE, SLEEVED_SHIRT_CHOICE
from .model_mixins import CrfModelMixin


class BaseRiskAssessmentSun (CrfModelMixin):

    hours_outdoor = models.CharField(
        verbose_name=('On average, how many hours are you outdoors per '
                      'day between 10am and 4pm?'),
        max_length=25,
        choices=HOURS_OUTDOOR_CHOICE,
    )

    sleeved_shirt = models.CharField(
        verbose_name=('When you are outside on a sunny day, how often '
                      'do you wear a SHIRT WITH SLEEVES?'),
        max_length=25,
        choices=SLEEVED_SHIRT_CHOICE,
    )

    hat = models.CharField(
        verbose_name=('When you are outside on a sunny day, how often '
                      'do you wear a HAT?'),
        max_length=25,
        choices=SLEEVED_SHIRT_CHOICE,
    )

    shade_umbrella = models.CharField(
        verbose_name=('When you are outside on a sunny day, how often '
                      'do you stay in the SHADE or UNDER AN UMBRELLA?'),
        max_length=25,
        choices=SLEEVED_SHIRT_CHOICE,
    )

    sunglasses = models.CharField(
        verbose_name=('When you are outside on a sunny day, how often '
                      'do you wear SUNGLASSES?'),
        max_length=25,
        choices=SLEEVED_SHIRT_CHOICE,
    )

    class Meta(CrfModelMixin.Meta):
        app_label = 'cancer_subject'
        verbose_name = 'Base Risk Assessment: Sun'
        verbose_name_plural = 'Base Risk Assessment: Sun'
