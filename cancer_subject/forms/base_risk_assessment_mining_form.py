from ..models import BaseRiskAssessmentMining
from .form_mixins import SubjectModelFormMixin


class BaseRiskAssessmentMiningForm (SubjectModelFormMixin):

    class Meta:
        model = BaseRiskAssessmentMining
        fields = '__all__'
