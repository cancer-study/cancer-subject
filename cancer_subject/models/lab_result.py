from django.db import models

from edc_constants.choices import YES_NO
from edc_base.model_fields import OtherCharField

from .model_mixins import CrfModelMixin


class LabResult (CrfModelMixin):

    """ CA005 Lab Result"""

    has_hiv_result = models.CharField(
        verbose_name=("Are there any new HIV TEST results that have "
                      "not been previously reported?"),
        max_length=3,
        choices=YES_NO,
        help_text="",
    )

    has_cd4 = models.CharField(
        verbose_name=("Are there any new CD4 CELL COUNT results that "
                      "have not been previously reported?"),
        max_length=3,
        choices=YES_NO,
        help_text="",
    )

    has_vl = models.CharField(
        verbose_name=("Are there any new HIV VIRAL LOAD results that "
                      "have not been previously reported?"),
        max_length=3,
        choices=YES_NO,
        help_text="",
    )

    has_haem = models.CharField(
        verbose_name=("Are there any new HAEMOTOLOGY results that have "
                      "not been previously reported?"),
        max_length=3,
        choices=YES_NO,
        help_text="",
    )

    has_chem = models.CharField(
        verbose_name=("Are there any new CHEMISTRY results that have "
                      "not been previously reported?"),
        max_length=3,
        choices=YES_NO,
        help_text="",
    )

    has_other_abnormal = models.CharField(
        verbose_name=("Are there any new OTHER ABNORMAL laboratory "
                      "results not been previously reported that have "
                      "changed or delayed planned treatment?"),
        max_length=3,
        choices=YES_NO,
        help_text="",
    )

    other_abnormal = OtherCharField()

    abnormal_lab_results = models.CharField(
        verbose_name=("Other abnormal lab results changing or "
                      "delaying planned treatment (record test, date, "
                      "result and units)"),
        max_length=65,
        help_text="",
    )

    tb_tests = models.CharField(
        verbose_name=("Are there any tuberculosis diagnostic tests "
                      "that have not been previously reported?"),
        max_length=3,
        choices=YES_NO,
        help_text="",
    )

    tb_prompt_other = OtherCharField()

    class Meta(CrfModelMixin.Meta):
        app_label = "cancer_subject"
        verbose_name = "Lab Result"
