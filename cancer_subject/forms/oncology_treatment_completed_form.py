from cancer_subject_validations.form_validators import OncologyTreatmentCompletedFormValidator

from ..models import OncologyTreatmentCompleted
from .modelform_mixin import SubjectModelFormMixin


class OncologyTreatmentCompletedForm (SubjectModelFormMixin):

    form_validator_cls = OncologyTreatmentCompletedFormValidator

    class Meta:
        model = OncologyTreatmentCompleted
        fields = '__all__'
