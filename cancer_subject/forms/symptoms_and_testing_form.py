from cancer_subject_validations.form_validators import SymptomsAndTestingFormValidator

from ..models import SymptomsAndTesting
from .form_mixins import SubjectModelFormMixin


class SymptomsAndTestingForm (SubjectModelFormMixin):

    form_validator_cls = SymptomsAndTestingFormValidator

    class Meta:
        model = SymptomsAndTesting
        fields = '__all__'
