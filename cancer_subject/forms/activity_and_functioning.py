from .modelform_mixin import SubjectModelFormMixin
from ..models import ActivityAndFunctioning

from cancer_subject_validations.form_validators import (
    ActivityAndFunctioningFormValidation)


class ActivityAndFunctioningForm (SubjectModelFormMixin):

    form_validator_cls = ActivityAndFunctioningFormValidation

    class Meta:
        model = ActivityAndFunctioning
        fields = '__all__'
