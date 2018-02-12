from ..models import BaseRiskAssessmentAlcohol
from .form_mixins import SubjectModelFormMixin


class BaseRiskAssessmentAlcoholForm (SubjectModelFormMixin):

    class Meta:
        model = BaseRiskAssessmentAlcohol
        fields = '__all__'
