from .form_mixins import SubjectModelFormMixin
from ..models import OTRChemo
from cancer_subject_validations.form_validators import (
    OTRChemoFormValidation
)


class OTRChemoForm (SubjectModelFormMixin):

    form_validator_cls = OTRChemoFormValidation

    class Meta:
        model = OTRChemo
        fields = '__all__'
