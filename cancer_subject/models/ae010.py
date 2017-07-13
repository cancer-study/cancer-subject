from django.db import models

from .model_mixins import CrfModelMixin

from ..choices.ae010 import (REPORT_TYPE_CHOICE,
                             RELATIONSHIP_DESCRIPTION_CHOICE)


class Ae010 (CrfModelMixin):

    report_type = models.CharField(
        verbose_name="1. Which type of report is this? ",
        max_length=35,
        choices=REPORT_TYPE_CHOICE,
        help_text="",
    )

    onset_date = models.DateTimeField(
        verbose_name="2. Date of onset of event being reported here:",
        max_length=25,
        help_text="",
    )

    event_grade = models.CharField(
        verbose_name="4. =Grade of primary event (use grading scale "
        "1-5, where 5=death) ",
        max_length=15,
        help_text="",
    )

    relationship_description = models.CharField(
        verbose_name="5. Please describe the relationship between "
        "this adverse event and study activities:",
        max_length=65,
        choices=RELATIONSHIP_DESCRIPTION_CHOICE,
        help_text="",
    )

    class Meta(CrfModelMixin.Meta):
        app_label = "cancer"
        verbose_name = "AE010 Adverse Event Report"
