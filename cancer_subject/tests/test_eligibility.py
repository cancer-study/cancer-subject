from django.test import TestCase
from edc_constants.constants import YES, NO

from ..eligibility import CancerStatusEvaluator


class TestSubjectScreening(TestCase):

    def test_eligibility_valid_cancer_status(self):
        status_evaluator = CancerStatusEvaluator(cancer_status=YES)
        self.assertTrue(status_evaluator.eligible)

    def test_eligibility_invalid_cancer_status(self):
        status_evaluator = CancerStatusEvaluator(cancer_status=NO)
        self.assertFalse(status_evaluator.eligible)

#     @tag('123')
#     def test_eligibility(self):
#         obj = Eligibility(
#             cancer_status=True)
#         self.assertTrue(obj.eligible)
