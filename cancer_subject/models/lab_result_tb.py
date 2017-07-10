# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail

from ..choices.lab_result import TB_TREATMENT_CHOICE
from .base_scheduled_visit_model import BaseScheduledVisitModel
from cancer_subject.models.model_mixins.crf_model_mixin import CrfModelMixin


class LabResultTb(CrfModelMixin):

    tb_description = models.CharField(
        verbose_name=("Describe tubercolosis diagnostic test results "
                      "(record test, date, result and units)"),
        max_length=65,
        help_text="",
        )

    tb_treatment = models.CharField(
        verbose_name=("Is participant being treated for tuberculosis "
                        "now?"),
        max_length=50,
        choices=TB_TREATMENT_CHOICE,
        help_text="",
        )

    tb_treatment_start = models.DateField(
        verbose_name=("When did the participant's treatment for "
                        "tuberculosis begin?"),
        max_length=25,
        null=True,
        blank=True,
        help_text="",
        )

    history = AuditTrail()

    def __unicode__(self):
        return unicode(self.subject_visit)

    def get_visit(self):
        return self.subject_visit

    def get_absolute_url(self):
        return reverse('admin:cancer_subject_labresulttb_change', args=(self.id,))

    class Meta:
        app_label = "cancer_subject"
        verbose_name = "Lab Result: Tubercolosis"
        verbose_name_plural = "Lab Result: Tubercolosis"
