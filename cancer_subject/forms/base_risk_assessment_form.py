from django import forms
from edc_constants.constants import YES

from ..models import BaseRiskAssessment

from .form_mixins import SubjectModelFormMixin


class BaseRiskAssessmentForm (SubjectModelFormMixin):
    def clean(self):

        cleaned_data = self.cleaned_data
        # validating tubercolosis
        if cleaned_data.get('tuberculosis') == YES and not cleaned_data.get('year_tb'):
            raise forms.ValidationError(
                'If patient has ever had tubercolosis, please provide the year TB was diagnosed')
        cleaned_data = super(BaseRiskAssessmentForm, self).clean()
        return cleaned_data

    class Meta:
        model = BaseRiskAssessment
        fields = '__all__'
