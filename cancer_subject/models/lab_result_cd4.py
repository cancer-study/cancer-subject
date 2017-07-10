# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

from edc.audit.audit_trail import AuditTrail
from .base_scheduled_visit_model import BaseScheduledVisitModel
from cancer_subject.models.model_mixins.crf_model_mixin import CrfModelMixin


class LabResultCd4(CrfModelMixin):

    cd4_drawn_date = models.DateField(
        verbose_name="5. Date of CD4 cell count",
        max_length=25,
        help_text="",
        )

    cd4_result = models.DecimalField(
        verbose_name="6. CD4 cell count result",
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(3000)],
        help_text="",
        )

    history = AuditTrail()

    def get_visit(self):
        return self.subject_visit

    def __unicode__(self):
        return unicode(self.subject_visit)

    def get_absolute_url(self):
        return reverse('admin:cancer_subject_labresultcd4_change', args=(self.id,))

    class Meta:
        app_label = "cancer_subject"
        verbose_name = "Lab Result: CD4"
        verbose_name_plural = "Lab Result: CD4"
