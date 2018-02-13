from django.db import models

from .model_mixins import CrfModelMixin

from cancer_subject.choice import HAART_STATUS_CHOICE


class HaartRecord(CrfModelMixin):

    """ MC034"""

#    hiv = models.CharField(
#        verbose_name="1. Does patient have HIV?",
#        max_length=9,
#        choices=YES_NO_DONT_KNOW,
#        help_text="",
#        )

    haart_status = models.CharField(
        verbose_name=("What is the status of the participant's "
                      "antiretroviral treatment (HAART)?"),
        max_length=145,
        null=True,
        blank=True,
        choices=HAART_STATUS_CHOICE,
        help_text="",
    )

    comments = models.TextField(
        verbose_name="Comments",
        max_length=150,
        null=True,
        blank=True,
        help_text="",
    )

    class Meta(CrfModelMixin.Meta):
        app_label = "cancer_subject"
        verbose_name = "Haart Record"
