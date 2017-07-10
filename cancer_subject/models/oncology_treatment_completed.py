from django.db import models
from django.core.urlresolvers import reverse

from edc.base.model.fields.custom.custom_fields import OtherCharField
from edc.audit.audit_trail import AuditTrail
from edc.choices.common import YES_NO_UNSURE

from .base_scheduled_visit_model import BaseScheduledVisitModel
from cancer_subject.models.model_mixins.crf_model_mixin import CrfModelMixin


class OncologyTreatmentCompleted (CrfModelMixin):

    """ NEW form on system upgrade"""

    patient_had_chemo = models.CharField(
        verbose_name=("Has the patient had chemotherapy?"),
        max_length=15,
        choices=YES_NO_UNSURE,
        help_text="",
        )

    patient_had_radiation = models.CharField(
        verbose_name=("Has the patient had radiation therapy?"),
        max_length=15,
        choices=YES_NO_UNSURE,
        help_text="",
        )

    patient_had_surgery = models.CharField(
        verbose_name=("Has the patient had surgery?"),
        max_length=15,
        choices=YES_NO_UNSURE,
        help_text="",
        )

    treatment_detail = models.TextField(
        verbose_name=("Describe any details of the treatment?"),
        max_length=150,
        null=True,
        blank=True,
        help_text="(dates, cycles, drugs, order of treatment, etc)",
        )

    patient_follow_up = models.CharField(
        verbose_name="Where is the patient being followed?",
        choices=(
            ('PMH', 'Princess Marina Hospital'),
            ('NRH', 'Nyangabgwe Referral Hospital'),
            ('SEROWE', 'Serowe'),
            ('MAUN', 'Maun'),
            ('Other', 'Other, specify'),),
        max_length=35
        )
    patient_follow_up_other = OtherCharField()

    next_followup = models.TextField(
        verbose_name="When does the patient have their next follow-up appointment?",
        max_length=50)

    history = AuditTrail()

    def get_visit(self):
        return self.subject_visit

    def __unicode__(self):
        return unicode(self.subject_visit)

    def get_absolute_url(self):
        return reverse('admin:cancer_subject_oncologytreatmentcompleted_change', args=(self.id,))

    class Meta:
        app_label = "cancer_subject"
        verbose_name = "Oncology Treatment Completed"
        verbose_name_plural = "Oncology Treatment Completed"
