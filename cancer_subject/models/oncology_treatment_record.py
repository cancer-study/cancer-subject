# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
from edc.choices.common import YES_NO
from .base_scheduled_visit_model import BaseScheduledVisitModel
from cancer_subject.models.model_mixins.crf_model_mixin import CrfModelMixin


class OncologyTreatmentRecord (CrfModelMixin):

    """ CA007 """
# v2 removed this first question
#    treatment_received = models.CharField(
#        verbose_name=("1. Has the patient received cancer treatment (chemotherapy, "
#                      "radiation, surgery) that has not yet been recorded?"),
#        max_length=3,
#        choices=YES_NO,
#        help_text="",
#        )

    chemo_received = models.CharField(
        verbose_name="Has the patient COMPLETED chemotherapy?",
        max_length=3,
        choices=YES_NO,
        help_text="",
        )

    radiation_received = models.CharField(
        verbose_name="Did the patient COMPLETE radiation therapy?",
        max_length=3,
        choices=YES_NO,
        help_text="",
        )

    surgical_therapy = models.CharField(
        verbose_name="Did patient COMPLETE surgical therapy?",
        max_length=3,
        choices=YES_NO,
        help_text="",
        )

    comments = models.CharField(
        verbose_name="Comments:",
        max_length=35,
        null=True,
        blank=True,
        help_text="",
        )

    history = AuditTrail()

    def get_visit(self):
        return self.subject_visit

    def __unicode__(self):
        return "%s" % self.subject_visit

    def get_absolute_url(self):
        return reverse('admin:cancer_subject_oncologytreatmentrecord_change', args=(self.id,))

    class Meta:
        app_label = "cancer_subject"
        verbose_name = "Oncology Treatment Record"
