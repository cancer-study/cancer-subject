from django import forms

from edc_constants.constants import YES

from .modelform_mixin import SubjectModelFormMixin
from ..models import OncologyTreatmentCompleted


class OncologyTreatmentCompletedForm (SubjectModelFormMixin):

    def clean(self):
        cleaned_data = self.cleaned_data

        if (cleaned_data.get('patient_had_chemo') == YES
                and not cleaned_data.get('treatment_detail')):
            raise forms.ValidationError(
                'Treatment is planned. Please provide details of the treatment')
        if (cleaned_data.get('patient_had_radiation') == YES
                and not cleaned_data.get('treatment_detail')):
            raise forms.ValidationError(
                'Treatment is planned. Please provide details of the treatment')
        if (cleaned_data.get('patient_had_surgery') == YES
                and not cleaned_data.get('treatment_detail')):
            raise forms.ValidationError(
                'Treatment is planned. Please provide details of the treatment')

        cleaned_data = super(OncologyTreatmentCompletedForm, self).clean()

        return cleaned_data

    class Meta:
        model = OncologyTreatmentCompleted
        fields = '__all__'
