from django.db import models

from .model_mixins import CrfModelMixin

from ..choices import OFF_STUDY_CODE_CHOICE


class Af004 (CrfModelMixin):

    date_off_study = models.DateTimeField(
        verbose_name="1. Date Participant off-study: ",
        max_length=25,
        help_text="dd/mm/yyyy",
    )

    date_last_contact = models.DateTimeField(
        verbose_name="2. Date of last contact: ",
        max_length=25,
        help_text="dd/mm/yyyy",
    )

    off_study_reason = models.CharField(
        verbose_name="3. Describe the primary reason for going off-study: ",
        max_length=35,
        help_text="",
    )

    off_study_code = models.CharField(
        verbose_name="4. Based on description above, code the primary reason for the Participant to be going off Study:",
        max_length=105,
        choices=OFF_STUDY_CODE_CHOICE,
        help_text="",
    )

    comments = models.CharField(
        verbose_name="6. Comments:",
        max_length=35,
    )

    class Meta(CrfModelMixin.Meta):
        app_label = "cancer_subject"
        verbose_name = "AF004 Off Study Record"
