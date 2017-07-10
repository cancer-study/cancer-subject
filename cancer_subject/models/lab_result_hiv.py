# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail

from ..choices.lab_result import TEST_RESULT_CHOICE
from .base_scheduled_visit_model import BaseScheduledVisitModel
from cancer_subject.models.model_mixins.crf_model_mixin import CrfModelMixin


class LabResultHiv(CrfModelMixin):

    test_date = models.DateField(
        verbose_name="2. Date of HIV test",
        max_length=25,
        null=True,
        blank=True,
        help_text=""
        )

    test_result = models.CharField(
        verbose_name="3. HIV test result",
        max_length=15,
        choices=TEST_RESULT_CHOICE,
        help_text="",
        )

    history = AuditTrail()

    def __unicode__(self):
        return unicode(self.subject_visit)

    def get_visit(self):
        return self.subject_visit

    def get_result_datetime(self):
        return self.test_date

#     def get_test_code(self):
#         return 'HIV'

#     def get_result_value(self, attr=None):
#         """Returns a result value for given attr name for the lab_tracker."""
#         retval = None
#         if not attr in dir(self):
#             raise TypeError('Attribute {0} does not exist in model {1}'.format(attr, self._meta.object_name))
#         if attr == 'hiv_result':
#             if self.test_result.lower() == 'pos':
#                 retval = 'POS'
#             elif self.test_result.lower() == 'neg':
#                 retval = 'NEG'
#             else:
#                 retval = 'UNK'
#         return retval

    def get_absolute_url(self):
        return reverse('admin:cancer_subject_labresulthiv_change', args=(self.id,))

    class Meta:
        app_label = "cancer_subject"
        verbose_name = "Lab Result: HIV"
        verbose_name_plural = "Lab Result: HIV"
