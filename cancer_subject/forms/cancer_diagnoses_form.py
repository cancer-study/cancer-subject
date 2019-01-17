from django import forms


from edc_constants.constants import YES, NO

from ..models import CancerDiagnosis
from .form_mixins import SubjectModelFormMixin
from cancer_subject_validations.form_validators import (
    CancerDiagnosisFormValidator
)

# CancerDiagnosis


class CancerDiagnosisForm (SubjectModelFormMixin):

    form_validator_cls = CancerDiagnosisFormValidator

    class Meta:
        model = CancerDiagnosis
        fields = '__all__'
