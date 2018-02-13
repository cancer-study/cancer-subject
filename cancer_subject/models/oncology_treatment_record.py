# coding: utf-8
from django.db import models

from edc_constants.choices import YES_NO

from .model_mixins import CrfModelMixin


class OncologyTreatmentRecord (CrfModelMixin):

    """ CA007 """
# v2 removed this first question
#    treatment_received = models.CharField(
#        verbose_name=("1. Has the patient received cancer treatment (chemotherapy, "
#                      "radiation, surgery) that has not yet been recorded?"),
#        max_length=3,
#        choices=YES_NO,
#        help_text="",
#        )

    chemo_received = models.CharField(
        verbose_name="Has the patient COMPLETED chemotherapy?",
        max_length=3,
        choices=YES_NO,
    )

    radiation_received = models.CharField(
        verbose_name="Did the patient COMPLETE radiation therapy?",
        max_length=3,
        choices=YES_NO,
    )

    surgical_therapy = models.CharField(
        verbose_name="Did patient COMPLETE surgical therapy?",
        max_length=3,
        choices=YES_NO,
    )

    comments = models.CharField(
        verbose_name="Comments:",
        max_length=35,
        null=True,
        blank=True,
    )

    class Meta(CrfModelMixin.Meta):
        app_label = "cancer_subject"
        verbose_name = "Oncology Treatment Record"
