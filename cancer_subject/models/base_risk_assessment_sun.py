from django.db import models

from .model_mixins import CrfModelMixin

from cancer_subject.choice import (
    HOURS_OUTDOOR_CHOICE, SLEEVED_SHIRT_CHOICE,
    HAT_CHOICE, SUNGLASSES_CHOICE, SHADE_UMBRELLA_CHOICE)


class BaseRiskAssessmentSun (CrfModelMixin):

    hours_outdoor = models.CharField(
        verbose_name=("On average, how many hours are you outdoors per "
                      "day between 10am and 4pm?"),
        max_length=15,
        choices=HOURS_OUTDOOR_CHOICE,
        help_text="",)

    sleeved_shirt = models.CharField(
        verbose_name=("When you are outside on a sunny day, how often "
                      "do you wear a SHIRT WITH SLEEVES?"),
        max_length=15,
        choices=SLEEVED_SHIRT_CHOICE,
        help_text="",)

    hat = models.CharField(
        verbose_name=("When you are outside on a sunny day, how often "
                      "do you wear a HAT?"),
        max_length=15,
        choices=HAT_CHOICE,
        help_text="",)

    shade_umbrella = models.CharField(
        verbose_name=("When you are outside on a sunny day, how often "
                      "do you stay in the SHADE or UNDER AN UMBRELLA?"),
        max_length=15,
        choices=SHADE_UMBRELLA_CHOICE,
        help_text="",)

    sunglasses = models.CharField(
        verbose_name=("When you are outside on a sunny day, how often "
                      "do you wear SUNGLASSES?"),
        max_length=15,
        choices=SUNGLASSES_CHOICE,
        help_text="",)

    class Meta(CrfModelMixin.Meta):
        app_label = "cancer_subject"
        verbose_name = "Base Risk Assessment: Sun"
        verbose_name_plural = "Base Risk Assessment: Sun"
