from ..models import BaseRiskAssessmentDemo
from .form_mixins import SubjectModelFormMixin


class BaseRiskAssessmentDemoForm (SubjectModelFormMixin):

    class Meta:
        model = BaseRiskAssessmentDemo
        fields = '__all__'
