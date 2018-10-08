from django import forms
from edc_constants.constants import YES

from ..models import BaseRiskAssessment

from .form_mixins import SubjectModelFormMixin


class BaseRiskAssessmentForm (SubjectModelFormMixin):

    class Meta:
        model = BaseRiskAssessment
        fields = '__all__'
