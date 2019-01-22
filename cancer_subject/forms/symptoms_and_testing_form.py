from django import forms
from edc_constants.constants import YES, NO

from ..models import SymptomsAndTesting
from .form_mixins import SubjectModelFormMixin
from cancer_subject_validations.form_validators import (
    SymptomsAndTestingFormValidator
)


class SymptomsAndTestingForm (SubjectModelFormMixin):

    form_validator_cls = SymptomsAndTestingFormValidator

    class Meta:
        model = SymptomsAndTesting
        fields = '__all__'
