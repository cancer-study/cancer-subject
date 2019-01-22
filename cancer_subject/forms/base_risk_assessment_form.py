from cancer_subject_validations.form_validators import (
    BaseRiskAssessmentFormValidator
)
from ..models import BaseRiskAssessment

from .form_mixins import SubjectModelFormMixin


class BaseRiskAssessmentForm (SubjectModelFormMixin):

    form_validator_cls = BaseRiskAssessmentFormValidator

    class Meta:
        model = BaseRiskAssessment
        fields = '__all__'
