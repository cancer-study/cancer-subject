# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
from edc.choices.common import YES_NO
from edc.base.model.fields.custom.custom_fields import OtherCharField

from ..choices.oncology_treatment import CHEMO_INTENT, WHY_DELAYED, WHY_REDUCED
from .base_scheduled_visit_model import BaseScheduledVisitModel
from cancer_subject.models.model_mixins.crf_model_mixin import CrfModelMixin


class OTRChemo (CrfModelMixin):

    chemo_intent = models.CharField(
        verbose_name="What was the intent of giving chemotherapy?",
        max_length=25,
        choices=CHEMO_INTENT,
        help_text="",
        )

    chemo_delays = models.CharField(
        verbose_name="Were any of the chemotherapy doses/cycles delayed?",
        max_length=3,
        choices=YES_NO,
        help_text="",
        )

    why_delayed = models.CharField(
        verbose_name="Why were the chemotherapy doses/cycles delayed?",
        max_length=65,
        choices=WHY_DELAYED,
        blank=True,
        help_text="",
        )
    why_delayed_other = OtherCharField()

    chemo_reduced = models.CharField(
        verbose_name="Were any of the chemotherapy doses (or number of cycles) reduced?",
        max_length=3,
        choices=YES_NO,
        help_text="",
        )

    why_reduced = models.CharField(
        verbose_name="Why were the chemotherapy doses (or number of cycles) reduced?",
        max_length=75,
        choices=WHY_REDUCED,
        blank=True,
        help_text="",
        )
    why_reduced_other = OtherCharField()

    history = AuditTrail()

    def __unicode__(self):
        return "%s" % self.subject_visit

    def get_visit(self):
        return self.subject_visit

    def get_absolute_url(self):
        return reverse('admin:cancer_subject_otrchemo_change', args=(self.id,))

    class Meta:
        app_label = "cancer_subject"
        verbose_name = "OTR: Chemotherapy"
        verbose_name_plural = "OTR: Chemotherapy"
