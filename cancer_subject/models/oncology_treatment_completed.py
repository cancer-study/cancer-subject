from django.db import models

from edc_base.model_fields import OtherCharField
from edc_constants.choices import YES_NO_UNSURE

from .model_mixins import CrfModelMixin

from ..choices import PATIENT_FOLLOW_UP


class OncologyTreatmentCompleted (CrfModelMixin):

    """ NEW form on system upgrade"""

    patient_had_chemo = models.CharField(
        verbose_name=('Has the patient had chemotherapy?'),
        max_length=15,
        choices=YES_NO_UNSURE,
    )

    patient_had_radiation = models.CharField(
        verbose_name=('Has the patient had radiation therapy?'),
        max_length=15,
        choices=YES_NO_UNSURE,
    )

    patient_had_surgery = models.CharField(
        verbose_name=('Has the patient had surgery?'),
        max_length=15,
        choices=YES_NO_UNSURE,
    )

    treatment_detail = models.TextField(
        verbose_name=('Describe any details of the treatment?'),
        max_length=150,
        null=True,
        blank=True,
        help_text='(dates, cycles, drugs, order of treatment, etc)',
    )

    patient_follow_up = models.CharField(
        verbose_name='Where is the patient being followed?',
        choices=PATIENT_FOLLOW_UP,
        max_length=35
    )
    patient_follow_up_other = OtherCharField()

    next_followup = models.TextField(
        verbose_name='When does the patient have their next '
        'follow-up appointment?',
        max_length=50)

    class Meta(CrfModelMixin.Meta):
        app_label = 'cancer_subject'
        verbose_name = 'Oncology Treatment Completed'
        verbose_name_plural = 'Oncology Treatment Completed'
