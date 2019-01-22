from django import forms

from edc_constants.constants import YES

from ..models import CurrentSymptoms
from .form_mixins import SubjectModelFormMixin

from cancer_subject_validations.form_validators import (
    CurrentSymptomsFormValidation
)


class CurrentSymptomsForm (SubjectModelFormMixin):

    form_validator_cls = CurrentSymptomsFormValidation

    class Meta:
        model = CurrentSymptoms
        fields = '__all__'
