from cancer_subject_validations.form_validators import CurrentSymptomsFormValidation

from ..models import CurrentSymptoms
from .form_mixins import SubjectModelFormMixin


class CurrentSymptomsForm (SubjectModelFormMixin):

    form_validator_cls = CurrentSymptomsFormValidation

    class Meta:
        model = CurrentSymptoms
        fields = '__all__'
