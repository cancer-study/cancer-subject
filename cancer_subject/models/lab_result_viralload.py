# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator

from edc.audit.audit_trail import AuditTrail
from .base_scheduled_visit_model import BaseScheduledVisitModel
from cancer_subject.models.model_mixins.crf_model_mixin import CrfModelMixin


class LabResultViralload(CrfModelMixin):

    vl_drawn_date = models.DateField(
        verbose_name="8. Date of HIV viral load",
        max_length=25,
        help_text="",
        )

    vl_result = models.CharField(
        verbose_name="9. HIV viral load result",
        max_length=25,
        validators=[RegexValidator(r'^[<>=]{1}\d+$', 'Result must include \
                                   the quantifier (<, > or =) followed by \
                                   the numeric value',), ],
        help_text="",
        )

    history = AuditTrail()

    def __unicode__(self):
        return unicode(self.subject_visit)

    def get_visit(self):
        return self.subject_visit

    def get_absolute_url(self):
        return reverse('admin:cancer_subject_labresultviralload_change', args=(self.id,))

    class Meta:
        app_label = "cancer_subject"
        verbose_name = "Lab Result: Viral Load"
        verbose_name_plural = "Lab Result: Viral Load"
