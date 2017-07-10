# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
from edc.choices.common import YES_NO_DONT_KNOW
from edc.base.model.fields.custom.custom_fields import OtherCharField

from .base_scheduled_visit_model import BaseScheduledVisitModel
from ..choices import FUEL_HOUSEHOLD20_CHOICE, FUEL_MONTH_CHOICE
from cancer_subject.models.model_mixins.crf_model_mixin import CrfModelMixin


class BaseRiskAssessmentFuel (CrfModelMixin):

    fuel_20y = models.CharField(
        verbose_name=("Over the past 20 years, what type of fuel was "
                        "used most for cooking/heating in your household?"),
        max_length=55,
        choices=FUEL_HOUSEHOLD20_CHOICE,
        help_text="",
        )
    fuel_20y_other = OtherCharField()

    cooking = models.CharField(
        verbose_name=("Over the past 20 years, was cooking usually "
                        "done indoors in your household?"),
        max_length=25,
        choices=YES_NO_DONT_KNOW,
        help_text="",
        )

    fuel_mm = models.CharField(
        verbose_name=("In the past month, what type of fuel was used "
                        "most for cooking / heating in your household?"),
        max_length=55,
        choices=FUEL_MONTH_CHOICE,
        help_text="",
        )
    fuel_mm_other = OtherCharField()

    cooking_mm = models.CharField(
        verbose_name=("In the past month, was cooking usually done "
                        "indoors in your household?"),
        max_length=25,
        choices=YES_NO_DONT_KNOW,
        help_text="",
        )

    history = AuditTrail()

    def get_visit(self):
        return self.subject_visit

    def __unicode__(self):
        return unicode(self.subject_visit)

    def get_absolute_url(self):
        return reverse('admin:cancer_subject_baseriskassessmentfuel_change', args=(self.id,))

    class Meta:
        app_label = "cancer_subject"
        verbose_name = "Base Risk Assessment: Fuel"
        verbose_name_plural = "Base Risk Assessment: Fuel"
