# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail

from .base_scheduled_visit_model import BaseScheduledVisitModel
from cancer_subject.models.model_mixins.crf_model_mixin import CrfModelMixin


class OTRSurgical (CrfModelMixin):

    operation_performed = models.CharField(
        verbose_name="What operation was performed?: ",
        max_length=100,
        help_text="",
        )

    date_operation = models.DateField(
        verbose_name="Date of operation?",
        max_length=15,
        blank=True,
        null=True,
        help_text="",
        )

    history = AuditTrail()

    def __unicode__(self):
        return "%s" % self.subject_visit

    def get_visit(self):
        return self.subject_visit

    def get_absolute_url(self):
        return reverse('admin:cancer_subject_otrsurgical_change', args=(self.id,))

    class Meta:
        app_label = "cancer_subject"
        verbose_name = "OTR: Surgical"
