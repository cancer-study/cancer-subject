from .modelform_mixin import SubjectModelFormMixin
from ..models import OncologyTreatmentPlan


class OncologyTreatmentPlanForm (SubjectModelFormMixin):

    class Meta:
        model = OncologyTreatmentPlan
        fields = '__all__'
