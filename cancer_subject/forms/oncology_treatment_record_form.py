from cancer_subject_validations.form_validators import (
    OncologyTreatmentRecordChemoFormValidation,
    OncologyTreatmentRecordRadiationFormValidation)

from .modelform_mixin import SubjectModelFormMixin
from ..models import (
    OncologyTreatmentRecord,
    OTRChemo,
    OTRRadiation,
    OTRSurgical)


class OncologyTreatmentRecordForm (SubjectModelFormMixin):

    class Meta:
        model = OncologyTreatmentRecord
        fields = '__all__'


class OTRChemoForm (SubjectModelFormMixin):

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data = OncologyTreatmentRecordChemoFormValidation(
            cleaned_data=cleaned_data).clean()
        return cleaned_data

    class Meta:
        model = OTRChemo
        fields = '__all__'


class OTRRadiationForm (SubjectModelFormMixin):

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data = OncologyTreatmentRecordRadiationFormValidation(
            cleaned_data=cleaned_data).clean()
        return cleaned_data

    class Meta:
        model = OTRRadiation
        fields = '__all__'


class OTRSurgicalForm (SubjectModelFormMixin):

    class Meta:
        model = OTRSurgical
        fields = '__all__'
