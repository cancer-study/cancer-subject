from django import forms
from edc_constants.constants import YES, NO

from ..models import OncologyTreatmentPlan
from .modelform_mixin import SubjectModelFormMixin


# OncologyTreatmentPlan
class OncologyTreatmentPlanForm (SubjectModelFormMixin):

    class Meta:
        model = OncologyTreatmentPlan
        fields = '__all__'
