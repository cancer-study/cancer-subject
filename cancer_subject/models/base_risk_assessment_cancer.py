from django.db import models

from edc_constants.choices import YES_NO_DONT_KNOW
from edc_base.model_fields.custom_fields import OtherCharField

from .model_mixins import CrfModelMixin

from ..choices.base_risk_assessment import (CANCER_TYPE_CHOICE,
                                            CANCER_BEFORE_CHOICE)


class BaseRiskAssessmentCancer (CrfModelMixin):

    family_cancer = models.CharField(
        verbose_name=("Has your son, daughter, brother, sister, or "
                      "parent ever had cancer?"),
        max_length=25,
        choices=YES_NO_DONT_KNOW,
        help_text="")

    family_cancer_type = models.CharField(
        verbose_name=("What kind of cancer did your brother, sister, "
                      "or parent have?"),
        max_length=45,
        choices=CANCER_TYPE_CHOICE,
        blank=True,
        help_text="",)

    family_cancer_other = OtherCharField()

    had_previous_cancer = models.CharField(
        verbose_name=("Have you had PREVIOUS cancer, before the "
                      "current cancer?"),
        max_length=25,
        choices=YES_NO_DONT_KNOW,
        help_text="")

    previous_cancer = models.CharField(
        verbose_name="What kind of cancer did you have before?",
        max_length=45,
        choices=CANCER_BEFORE_CHOICE,
        blank=True,
        help_text="",)

    previous_cancer_other = OtherCharField()

    class Meta(CrfModelMixin.Meta):
        app_label = "cancer_subject"
        verbose_name = "Base Risk Assessment: Cancer"
        verbose_name_plural = "Base Risk Assessment: Cancer"
