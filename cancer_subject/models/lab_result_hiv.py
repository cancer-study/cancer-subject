from django.db import models

from .model_mixins import CrfModelMixin

from ..choices import TEST_RESULT_CHOICE


class LabResultHiv(CrfModelMixin):

    test_date = models.DateField(
        verbose_name='Date of HIV test',
        max_length=25,
        null=True,
        blank=True,
    )

    test_result = models.CharField(
        verbose_name='HIV test result',
        max_length=15,
        choices=TEST_RESULT_CHOICE,
    )

    def get_test_code(self):
        return 'HIV'

#     def get_result_value(self, attr=None):
#         '''Returns a result value for given attr name for the lab_tracker.'''
#         retval = None
#         if not attr in dir(self):
#             raise TypeError('Attribute {0} does not exist in model {1}'.format(
#                 attr, self._meta.object_name))
#         if attr == 'hiv_result':
#             if self.test_result.lower() == 'pos':
#                 retval = 'POS'
#             elif self.test_result.lower() == 'neg':
#                 retval = 'NEG'
#             else:
#                 retval = 'UNK'
#         return retval

    class Meta(CrfModelMixin.Meta):
        app_label = 'cancer_subject'
        verbose_name = 'Lab Result: HIV'
        verbose_name_plural = 'Lab Result: HIV'
