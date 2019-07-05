from django.db import models
from edc_base.model_managers.historical_records import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators.date import date_not_future

from ..choices import DRUG_CODE, DOSE_CATEGORY, NUMBER_OF_CHEMO_CYLCES
from ..choices import NUMBER_OF_CHEMO_INTERVALS
from .oncology_treatment_plan import OncologyTreatmentPlan
from .otr_chemo import OTRChemo


class BaseChemoMedication(BaseUuidModel):

    drug_code = models.CharField(
        verbose_name='Drug:',
        max_length=35,
        choices=DRUG_CODE,
    )

    dose_category = models.CharField(
        verbose_name='Dose category:',
        max_length=35,
        null=True,
        blank=True,
        choices=DOSE_CATEGORY,
    )

    start_date = models.DateField(
        verbose_name='Date that chemotherapy was started:',
        max_length=35,
        validators=[date_not_future],
    )

    stop_date = models.DateField(
        verbose_name='Date of last chemotherapy dose:',
        max_length=35,
        validators=[date_not_future],
        null=True,
        blank=True,

    )

    cycle_num = models.CharField(
        verbose_name='Number of completed cycles:',
        max_length=15,
        null=True,
        blank=True,
        choices=NUMBER_OF_CHEMO_CYLCES,
        help_text=('Enter number of planned cycles or chemotherapy '
                   'treatments. For continuous treatments (like tamoxifen, '
                   'leuprolide, hydrooxyurea) record as 1 cycle.'),
    )

    interval = models.CharField(
        verbose_name='Interval:',
        max_length=15,
        null=True,
        blank=True,
        choices=NUMBER_OF_CHEMO_INTERVALS,
        help_text=('Enter number of days between planned cycle (from day '
                   '1 of cycle 1 to day 1 of cycle 2). For single cycle '
                   'treatments or continuous treatments record as -3.'),
    )

    specify_other_med = models.CharField(
        max_length=35,
        verbose_name='Specify other medication:',
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True


class ChemoMedPlanManager(models.Manager):

    def get_by_natural_key(self, drug_code, dose_category, subject_identifier,
                           visit_schedule_name, schedule_name, visit_code):
        return self.get(
            drug_code=drug_code,
            dose_category=dose_category,
            subject_visit__subject_identifier=subject_identifier,
            subject_visit__visit_schedule_name=visit_schedule_name,
            subject_visit__schedule_name=schedule_name,
            subject_visit__visit_code=visit_code)


class ChemoMedPlan(BaseChemoMedication):

    oncology_treatment_plan = models.ForeignKey(
        OncologyTreatmentPlan,
        on_delete=models.PROTECT)

    history = HistoricalRecords()

    objects = ChemoMedPlanManager()

    def natural_key(self):
        return (self.drug_code, self.dose_category) + self.oncology_treatment_plan.natural_key()
    natural_key.dependencies = ['cancer_subject.oncology_treatment_plan']

    class Meta:
        app_label = 'cancer_subject'
        verbose_name = 'Chemo Medication Plan'
        unique_together = ('oncology_treatment_plan',
                           'drug_code', 'dose_category')


class ChemoMedRecordManager(models.Manager):

    def get_by_natural_key(self, drug_code, dose_category, subject_identifier,
                           visit_schedule_name, schedule_name, visit_code):
        return self.get(
            drug_code=drug_code,
            dose_category=dose_category,
            subject_visit__subject_identifier=subject_identifier,
            subject_visit__visit_schedule_name=visit_schedule_name,
            subject_visit__schedule_name=schedule_name,
            subject_visit__visit_code=visit_code)


class ChemoMedRecord(BaseChemoMedication):

    otr_chemo = models.ForeignKey(
        OTRChemo,
        on_delete=models.PROTECT)

    history = HistoricalRecords()

    objects = ChemoMedRecordManager()

    def natural_key(self):
        return (self.drug_code, self.dose_category) + self.otr_chemo.natural_key()
    natural_key.dependencies = ['cancer_subject.oncology_treatment_plan']

    class Meta:
        app_label = 'cancer_subject'
        verbose_name = 'Chemo Medication Record'
        unique_together = ('otr_chemo', 'drug_code', 'dose_category')
