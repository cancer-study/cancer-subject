from django.apps import apps as django_apps
from django.test import TestCase, tag
from edc_constants.constants import FEMALE, YES, MALE, ABNORMAL, NORMAL, NO
from model_mommy import mommy
from cancer_subject.eligibility import AgeEvaluator


@tag('screening')
class TestSubjectScreening(TestCase):

    def setUp(self):
        django_apps.app_configs[
            'cancer_subject'].screening_age_adult_upper = 99
        django_apps.app_configs[
            'cancer_subject'].screening_age_adult_lower = 18