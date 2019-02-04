from cancer_subject_validations.form_validators import LabResultTbFormValidator

from ..models import LabResultTb
from .form_mixins import SubjectModelFormMixin


class LabResultTbForm(SubjectModelFormMixin):

    form_validator_cls = LabResultTbFormValidator

    class Meta:
        model = LabResultTb
        fields = '__all__'
