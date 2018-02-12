from ..models import BaseRiskAssessmentSun
from .form_mixins import SubjectModelFormMixin


class BaseRiskAssessmentSunForm (SubjectModelFormMixin):

    class Meta:
        model = BaseRiskAssessmentSun
        fields = '__all__'
