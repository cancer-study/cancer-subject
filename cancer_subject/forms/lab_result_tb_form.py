from django import forms

from ..models import LabResultTb
from .form_mixins import SubjectModelFormMixin


class LabResultTbForm(SubjectModelFormMixin):

    def clean(self):
        cleaned_data = self.cleaned_data
        treatment1 = 'Yes, isoniazid preventative therapy (IPT)'
        treatment2 = 'Yes, combination anti-tuberculosis treatment (ATT)'
        if (cleaned_data['tb_treatment'] == treatment1
                and not cleaned_data['tb_treatment_start']):
            raise forms.ValidationError(
                'If participant is receiving any kind of treatment, when did '
                'this treatment begin')
        if (cleaned_data['tb_treatment'] == treatment2
                and not cleaned_data['tb_treatment_start']):
            raise forms.ValidationError(
                'If participant is receiving any kind of treatment, when did '
                'this treatment begin')
        cleaned_data = super(LabResultTbForm, self).clean()
        return cleaned_data

    class Meta:
        model = LabResultTb
        fields = '__all__'
