# coding: utf-8
from django.db import models

from edc_constants.choices import YES_NO
from edc_base.model_fields import OtherCharField

from .model_mixins import CrfModelMixin

<<<<<<< Updated upstream
from ..choices import (CHEMO_INTENT,
                       WHY_DELAYED,
                       WHY_REDUCED)
=======
from cancer_subject.choice import (CHEMO_INTENT,
                                          WHY_DELAYED,
                                          WHY_REDUCED)
>>>>>>> Stashed changes


class OTRChemo (CrfModelMixin):

    chemo_intent = models.CharField(
        verbose_name="What was the intent of giving chemotherapy?",
        max_length=25,
        choices=CHEMO_INTENT,
        help_text="",
    )

    chemo_delays = models.CharField(
        verbose_name="Were any of the chemotherapy doses/cycles "
        "delayed?",
        max_length=3,
        choices=YES_NO,
        help_text="",
    )

    why_delayed = models.CharField(
        verbose_name="Why were the chemotherapy doses/cycles delayed?",
        max_length=65,
        choices=WHY_DELAYED,
        blank=True,
        help_text="",
    )
    why_delayed_other = OtherCharField()

    chemo_reduced = models.CharField(
        verbose_name="Were any of the chemotherapy doses (or number "
        "of cycles) reduced?",
        max_length=3,
        choices=YES_NO,
        help_text="",
    )

    why_reduced = models.CharField(
        verbose_name="Why were the chemotherapy doses (or number of "
        "cycles) reduced?",
        max_length=75,
        choices=WHY_REDUCED,
        blank=True,
        help_text="",
    )
    why_reduced_other = OtherCharField()

    class Meta(CrfModelMixin.Meta):
        app_label = "cancer_subject"
        verbose_name = "OTR: Chemotherapy"
        verbose_name_plural = "OTR: Chemotherapy"
