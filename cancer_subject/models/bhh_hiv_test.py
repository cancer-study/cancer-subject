from django.db import models

from edc_constants.choices import YES_NO

from .model_mixins import CrfModelMixin

from ..choices.baseline_hiv_history import RECENT_RESULT_CHOICE


class BHHHivTest (CrfModelMixin):

    hiv_drawn_date = models.DateField(
        verbose_name="Date of most recent HIV test:",
        max_length=25,
        help_text="",
    )
    # v2 added field for when exact date is unknown
    hiv_testdate_est = models.CharField(
        verbose_name="Is the HIV test date estimated?",
        max_length=3,
        choices=YES_NO,
        help_text="",)

    hiv_result = models.CharField(
        verbose_name=("Result of most recent HIV test:"),
        max_length=50,
        choices=RECENT_RESULT_CHOICE,
        help_text=("If last HIV test negative (or Don't Know) and "
                   "more than six months ago, perform HIV testing "
                   "unless patient refuses."),)

    class Meta(CrfModelMixin.Meta):
        app_label = "cancer_subject"
        verbose_name = "BHH: HIV Test"
