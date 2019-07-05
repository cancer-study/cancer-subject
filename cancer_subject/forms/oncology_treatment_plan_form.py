from cancer_subject_validations.form_validators import OncologyTreatmentPlanFormValidator

from ..models import OncologyTreatmentPlan
from .modelform_mixin import SubjectModelFormMixin


class OncologyTreatmentPlanForm (SubjectModelFormMixin):

    form_validator_cls = OncologyTreatmentPlanFormValidator

    class Meta:
        model = OncologyTreatmentPlan
        fields = '__all__'
