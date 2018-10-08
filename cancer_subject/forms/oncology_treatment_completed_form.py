from django import forms
from edc_constants.constants import YES

from ..models import OncologyTreatmentCompleted
from .modelform_mixin import SubjectModelFormMixin


class OncologyTreatmentCompletedForm (SubjectModelFormMixin):

    class Meta:
        model = OncologyTreatmentCompleted
        fields = '__all__'
