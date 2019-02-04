from cancer_subject_validations.form_validators import OTRChemoFormValidation

from ..models import OTRChemo
from .form_mixins import SubjectModelFormMixin


class OTRChemoForm (SubjectModelFormMixin):

    form_validator_cls = OTRChemoFormValidation

    class Meta:
        model = OTRChemo
        fields = '__all__'
