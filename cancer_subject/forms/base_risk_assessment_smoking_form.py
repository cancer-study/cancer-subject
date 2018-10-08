from django import forms

from ..models import BaseRiskAssessmentSmoking
from .form_mixins import SubjectModelFormMixin


# BaseRiskAssessmentSmoking
class BaseRiskAssessmentSmokingForm (SubjectModelFormMixin):

    class Meta:
        model = BaseRiskAssessmentSmoking
        fields = '__all__'
