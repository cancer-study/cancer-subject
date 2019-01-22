from ..models import BaseRiskAssessmentFemale
from .form_mixins import SubjectModelFormMixin
from cancer_subject_validations.form_validators import (
    BaseRiskAssessmentFemaleValidation
)


class BaseRiskAssessmentFemaleForm (SubjectModelFormMixin):

    form_validator_cls = BaseRiskAssessmentFemaleValidation

    class Meta:
        model = BaseRiskAssessmentFemale
        fields = '__all__'
