# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
from edc.choices.common import YES_NO

from .base_scheduled_visit_model import BaseScheduledVisitModel
from cancer_subject.models.model_mixins.crf_model_mixin import CrfModelMixin


class OTRRadiation (CrfModelMixin):

    radiation_details = models.CharField(
        verbose_name="Are there radiation details available?",
        max_length=3,
        choices=YES_NO,
        help_text="",
        )

#     concomitant = models.CharField(
#         verbose_name="10. Was radiation given at the same time (concomitant) as chemotherapy?",
#         max_length=3,
#         null=True,
#         blank=True,
#         choices=YES_NO,
#         help_text="",
#         )
#
#     amount_radiation = models.CharField(
#         verbose_name="11. How many radiation treatments were received?",
#         null=True,
#         blank=True,
#         max_length=15,
#         help_text="",
#         )

    history = AuditTrail()

    def __unicode__(self):
        return "%s" % self.subject_visit

    def get_visit(self):
        return self.subject_visit

    def get_absolute_url(self):
        return reverse('admin:cancer_subject_otrradiation_change', args=(self.id,))

    class Meta:
        app_label = "cancer_subject"
        verbose_name = "OTR: Radiation"
