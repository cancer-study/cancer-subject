from cancer_subject_validations.form_validators import CancerDiagnosisFormValidator

from ..models import CancerDiagnosis
from .form_mixins import SubjectModelFormMixin


# CancerDiagnosis
class CancerDiagnosisForm (SubjectModelFormMixin):

    form_validator_cls = CancerDiagnosisFormValidator

    class Meta:
        model = CancerDiagnosis
        fields = '__all__'
