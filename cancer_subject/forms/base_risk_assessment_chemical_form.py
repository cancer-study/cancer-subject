from django import forms
from edc_constants.constants import YES

from ..models import BaseRiskAssessmentChemical
from .form_mixins import SubjectModelFormMixin


class BaseRiskAssessmentChemicalForm (SubjectModelFormMixin):
    def clean(self):
        cleaned_data = self.cleaned_data
        if cleaned_data.get('asbestos') == YES and not cleaned_data.get('asbestos_no_protection'):
            raise forms.ValidationError(
                'If subject has worked with asbestos, how long has he/she worked with it')
        if cleaned_data.get('chemicals') == YES and not cleaned_data.get('chemicals_time'):
            raise forms.ValidationError(
                'If subject has worked with any of the chemicals, how long has it been')
        if cleaned_data.get('arsenic_smelting') == YES and not cleaned_data.get('total_time_no_protection'):
            raise forms.ValidationError(
                'If subject has ever been involved in arsenic smelting, how long has it been')
        cleaned_data = super(BaseRiskAssessmentChemicalForm, self).clean()
        return cleaned_data

    class Meta:
        model = BaseRiskAssessmentChemical
        fields = '__all__'
