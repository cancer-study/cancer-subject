from django import forms
from edc_constants.constants import YES

from ..models import BaseRiskAssessmentChemical
from .form_mixins import SubjectModelFormMixin


class BaseRiskAssessmentChemicalForm (SubjectModelFormMixin):

    class Meta:
        model = BaseRiskAssessmentChemical
        fields = '__all__'
