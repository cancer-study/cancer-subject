from django import forms
from edc_constants.constants import YES

from ..models import OncologyTreatmentCompleted
from .modelform_mixin import SubjectModelFormMixin

from cancer_subject_validations.form_validators import (
    OncologyTreatmentCompletedFormValidator
)


class OncologyTreatmentCompletedForm (SubjectModelFormMixin):

    form_validator_cls = OncologyTreatmentCompletedFormValidator

    class Meta:
        model = OncologyTreatmentCompleted
        fields = '__all__'
