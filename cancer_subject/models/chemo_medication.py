from django.db import models

from ..managers import ChemoMedPlanManager, ChemoMedRecordManager

from ..choices.oncology_treatment import (DRUG_CODE,
                                          DOSE_CATEGORY,
                                          NUMBER_OF_CHEMO_CYLCES,
                                          NUMBER_OF_CHEMO_INTERVALS)
from .subject_base_uuid_model import SubjectBaseUuidModel
from .oncology_treatment_plan import OncologyTreatmentPlan
from .otr_chemo import OTRChemo


class BaseChemoMedication(SubjectBaseUuidModel):

    drug_code = models.CharField(
        verbose_name="Drug",
        max_length=35,
        choices=DRUG_CODE,
        help_text="",
    )
    dose_category = models.CharField(
        verbose_name="Dose category",
        max_length=35,
        null=True,
        blank=True,
        choices=DOSE_CATEGORY,
    )
    start_date = models.DateField(
        verbose_name="Date that chemotherapy was started",
        max_length=35,
    )
    # newly_added
    stop_date = models.DateField(
        verbose_name="Date of last chemotherapy dose",
        null=True,
        blank=True,
        max_length=35,
    )
    cycle_num = models.CharField(
        verbose_name="Number of completed cycles",
        max_length=15,
        null=True,
        blank=True,
        choices=NUMBER_OF_CHEMO_CYLCES,
        help_text=("Enter number of planned cycles or chemotherapy "
                   "treatments. For continuous treatments (like tamoxifen, "
                   "leuprolide, hydrooxyurea) record as 1 cycle. "),
    )
    interval = models.CharField(
        verbose_name="Interval",
        max_length=15,
        null=True,
        blank=True,
        choices=NUMBER_OF_CHEMO_INTERVALS,
        help_text=("Enter number of days between planned cycle (from day "
                   "1 of cycle 1 to day 1 of cycle 2). For single cycle "
                   "treatments or continuous treatments record as -3. "),
    )
    specify_other_med = models.CharField(
        max_length=35,
        verbose_name="Specify other medication:",
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True


class ChemoMedPlan(BaseChemoMedication):

    oncology_treatment_plan = models.ForeignKey(OncologyTreatmentPlan)

    objects = ChemoMedPlanManager()

    class Meta:
        app_label = "cancer_subject"
        verbose_name = "Chemo Medication Plan"


class ChemoMedRecord(BaseChemoMedication):

    otr_chemo = models.ForeignKey(OTRChemo)

    objects = ChemoMedRecordManager()

    class Meta:
        app_label = "cancer_subject"
        verbose_name = "Chemo Medication Record"
