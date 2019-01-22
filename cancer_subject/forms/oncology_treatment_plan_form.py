from django import forms
from edc_constants.constants import YES, NO

from ..models import OncologyTreatmentPlan
from .modelform_mixin import SubjectModelFormMixin
from cancer_subject_validations.form_validators import (
    OncologyTreatmentPlanFormValidator
)

# OncologyTreatmentPlan


class OncologyTreatmentPlanForm (SubjectModelFormMixin):

    form_validator_cls = OncologyTreatmentPlanFormValidator

    class Meta:
        model = OncologyTreatmentPlan
        fields = '__all__'
