from cancer_subject_validations.form_validators import (
    BaseRiskAssessmentCancerFormValidation)

from ..models import BaseRiskAssessmentCancer
from .form_mixins import SubjectModelFormMixin


class BaseRiskAssessmentCancerForm (SubjectModelFormMixin):

    form_validator_cls = BaseRiskAssessmentCancerFormValidation

    class Meta:
        model = BaseRiskAssessmentCancer
        fields = '__all__'
