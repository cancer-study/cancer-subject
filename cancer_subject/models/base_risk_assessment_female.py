# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
from edc.choices.common import YES_NO

from .base_scheduled_visit_model import BaseScheduledVisitModel
from cancer_subject.models.model_mixins.crf_model_mixin import CrfModelMixin


class BaseRiskAssessmentFemale (CrfModelMixin):

    age_period = models.IntegerField(
        verbose_name=("At what age did you start having your menstrual period?"),
        help_text="",)

    children = models.IntegerField(
        verbose_name="How many children have you given birth to?",
        help_text="")

    years_breastfed = models.CharField(
        verbose_name=("Have you breastfed for a total of at least 1 "
                        "year?  If you have more than 1 child, this includes "
                        "time spent breast feeding all your children."),
        max_length=3,
        choices=YES_NO,
        help_text="",)

    class Meta:
        app_label = "cancer_subject"
        verbose_name = "Base Risk Assessment: Female"
        verbose_name_plural = "Base Risk Assessment: Female"
