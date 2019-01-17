from cancer_subject_validations.form_validators import (
    BaseRiskAssessmentSmokingFormValidation
)
from ..models import BaseRiskAssessmentSmoking
from .form_mixins import SubjectModelFormMixin


# BaseRiskAssessmentSmoking
class BaseRiskAssessmentSmokingForm (SubjectModelFormMixin):

    form_validator_cls = BaseRiskAssessmentSmokingFormValidation

    class Meta:
        model = BaseRiskAssessmentSmoking
        fields = '__all__'
