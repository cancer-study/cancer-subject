from ..models import LabResultHeightWeight
from .form_mixins import SubjectModelFormMixin
from cancer_subject_validations.form_validators import (
    LabResultsHeightWeightValidator)


class LabResultHeightWeightForm(SubjectModelFormMixin):

    form_validator_cls = LabResultsHeightWeightValidator

    class Meta:
        model = LabResultHeightWeight
        fields = '__all__'
