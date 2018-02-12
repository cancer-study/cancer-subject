from ..models import BaseRiskAssessmentFemale
from .form_mixins import SubjectModelFormMixin


class BaseRiskAssessmentFemaleForm (SubjectModelFormMixin):

    class Meta:
        model = BaseRiskAssessmentFemale
        fields = '__all__'
