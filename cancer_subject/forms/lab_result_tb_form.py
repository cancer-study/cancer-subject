from django import forms

from ..models import LabResultTb
from .form_mixins import SubjectModelFormMixin


class LabResultTbForm(SubjectModelFormMixin):

    def clean(self):
        cleaned_data = self.cleaned_data
        if (cleaned_data['tb_treatment'] == 'Yes, isoniazid preventative therapy (IPT)'
                and not cleaned_data['tb_treatment_start']):
            raise forms.ValidationError(
                'If participant is receiving any kind of treatment, when did '
                'this treatment begin')
        if (cleaned_data['tb_treatment'] == 'Yes, combination anti-tuberculosis'
                ' treatment (ATT)' and not cleaned_data['tb_treatment_start']):
            raise forms.ValidationError(
                'If participant is receiving any kind of treatment, when did '
                'this treatment begin')
        cleaned_data = super(LabResultTbForm, self).clean()
        return cleaned_data

    class Meta:
        model = LabResultTb
        fields = '__all__'
