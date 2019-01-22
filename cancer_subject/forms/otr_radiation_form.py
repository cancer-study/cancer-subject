from .form_mixins import SubjectModelFormMixin
from ..models import OTRRadiation

from cancer_subject_validations.form_validators import (
    OTRRadiationFormValidation
)


class OTRRadiationForm (SubjectModelFormMixin):

    form_validator_cls = OTRRadiationFormValidation

    class Meta:
        model = OTRRadiation
        fields = '__all__'
