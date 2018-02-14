from ..models import BaseRiskAssessmentEating
#from .form_mixins import SubjectModelFormMixin


class BaseRiskAssessmentEatingForm:  # (SubjectModelFormMixin):

    class Meta:
        model = BaseRiskAssessmentEating
        fields = '__all__'
