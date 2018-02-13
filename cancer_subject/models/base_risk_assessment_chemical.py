from django.db import models

from edc_constants.choices import YES_NO_DONT_KNOW

from .model_mixins.crf_model_mixin import CrfModelMixin

from ..choices import (ASBESTOS_NO_PROTECTION_CHOICE, CHEMICALS_TIME_CHOICE,
                       TOTAL_TIME_NO_PROTECTION_CHOICE)


class BaseRiskAssessmentChemical (CrfModelMixin):

    """ chemical exposure """
    asbestos = models.CharField(
        verbose_name=("Have you ever worked with asbestos without "
                      "adequate protection?"),
        max_length=25,
        choices=YES_NO_DONT_KNOW,
        help_text="",)

    asbestos_no_protection = models.CharField(
        verbose_name=("What is the total amount of time you worked "
                      "with asbestos without protection?"),
        max_length=25,
        choices=ASBESTOS_NO_PROTECTION_CHOICE,
        blank=True,
        help_text="",)

    chemicals = models.CharField(
        verbose_name=("Have you ever worked with any of these "
                      "chemical without adequate protection?"),
        max_length=25,
        choices=YES_NO_DONT_KNOW,
        help_text=("Radon, Cadmium, Chromium, Beryllium, Aluminum, "
                   "Silica, Sulfuric acid, mist, chloromethyl ether, "
                   "coke (fuel from coal), mustard gas"),)

    chemicals_time = models.CharField(
        verbose_name=("What is the total amount of time you worked "
                      "with the chemical(s) without protection?"),
        max_length=25,
        choices=CHEMICALS_TIME_CHOICE,
        blank=True,
        help_text="",)

    arsenic_smelting = models.CharField(
        verbose_name=("Have you ever been involved with arsenic "
                      "smelting (nickel and copper), coal "
                      "gasification, or iron/steel founding without "
                      "adequate protection? "),
        max_length=25,
        choices=YES_NO_DONT_KNOW,
        help_text="",)

    total_time_no_protection = models.CharField(
        verbose_name=("What is the total amount of time you worked "
                      "with the process(es) without protection?"),
        max_length=25,
        choices=TOTAL_TIME_NO_PROTECTION_CHOICE,
        blank=True,
        help_text="",)

    class Meta(CrfModelMixin.Meta):
        app_label = "cancer_subject"
        verbose_name = "Base Risk Assessment: Chemicals"
        verbose_name_plural = "Base Risk Assessment: Chemicals"
