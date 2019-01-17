
from cancer_subject_validations.form_validators import (
    BaseRiskAssessmentChemicalValidation
)
from ..models import BaseRiskAssessmentChemical
from .form_mixins import SubjectModelFormMixin


class BaseRiskAssessmentChemicalForm (SubjectModelFormMixin):

    form_validator_cls = BaseRiskAssessmentChemicalValidation

    class Meta:
        model = BaseRiskAssessmentChemical
        fields = '__all__'
