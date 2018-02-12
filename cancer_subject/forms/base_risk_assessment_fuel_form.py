from ..models import BaseRiskAssessmentFuel
from .form_mixins import SubjectModelFormMixin


class BaseRiskAssessmentFuelForm (SubjectModelFormMixin):

    class Meta:
        model = BaseRiskAssessmentFuel
        fields = '__all__'
