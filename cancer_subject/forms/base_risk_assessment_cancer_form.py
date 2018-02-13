from django import forms
from edc_constants.constants import YES

from ..models import BaseRiskAssessmentCancer
from .form_mixins import SubjectModelFormMixin


# BaseRiskAssessmentCancer
class BaseRiskAssessmentCancerForm (SubjectModelFormMixin):
    def clean(self):
        cleaned_data = self.cleaned_data
        if (cleaned_data.get('family_cancer') == YES
                and not cleaned_data.get('family_cancer_type')):
            raise forms.ValidationError(
                'If any relative has had any cancer, what type was it')
        if (cleaned_data.get('had_previous_cancer') == YES
                and not cleaned_data.get('previous_cancer')):
            raise forms.ValidationError('If subject has had a previous'
                                        ' cancer, what kind of cancer was it')
        cleaned_data = super(BaseRiskAssessmentCancerForm, self).clean()
        return cleaned_data

    class Meta:
        model = BaseRiskAssessmentCancer
        fields = '__all__'
