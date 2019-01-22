from django import forms

from ..models import LabResultTb
from .form_mixins import SubjectModelFormMixin
from cancer_subject_validations.form_validators import (
    LabResultTbFormValidator
)


class LabResultTbForm(SubjectModelFormMixin):

    form_validator_cls = LabResultTbFormValidator

    class Meta:
        model = LabResultTb
        fields = '__all__'
