# coding: utf-8
from django.db import models

from edc_constants.choices import YES_NO

from .model_mixins import CrfModelMixin


class OTRRadiation (CrfModelMixin):

    radiation_details = models.CharField(
        verbose_name="Are there radiation details available?",
        max_length=3,
        choices=YES_NO,
        help_text="",
    )

#     concomitant = models.CharField(
#         verbose_name="10. Was radiation given at the same time (concomitant) as chemotherapy?",
#         max_length=3,
#         null=True,
#         blank=True,
#         choices=YES_NO,
#         help_text="",
#         )
#
#     amount_radiation = models.CharField(
#         verbose_name="11. How many radiation treatments were received?",
#         null=True,
#         blank=True,
#         max_length=15,
#         help_text="",
#         )

    class Meta(CrfModelMixin.Meta):
        app_label = "cancer_subject"
        verbose_name = "OTR: Radiation"
