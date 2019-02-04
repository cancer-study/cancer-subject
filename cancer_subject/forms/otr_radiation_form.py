from cancer_subject_validations.form_validators import OTRRadiationFormValidation

from ..models import OTRRadiation
from .form_mixins import SubjectModelFormMixin


class OTRRadiationForm (SubjectModelFormMixin):

    form_validator_cls = OTRRadiationFormValidation

    class Meta:
        model = OTRRadiation
        fields = '__all__'
