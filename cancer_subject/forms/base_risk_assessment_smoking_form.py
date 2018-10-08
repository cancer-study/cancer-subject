from django import forms

from ..models import BaseRiskAssessmentSmoking
from .form_mixins import SubjectModelFormMixin


# BaseRiskAssessmentSmoking
class BaseRiskAssessmentSmokingForm (SubjectModelFormMixin):
    def clean(self):
        cleaned_data = super(BaseRiskAssessmentSmokingForm, self).clean()

        if (cleaned_data.get('smoke_now') == 'no'
                and cleaned_data.get('cigarette_smoking')):
            raise forms.ValidationError('Subject quit smoking. DO NOT give '
                                        'any details about smoking NOW.')
        if (cleaned_data.get('smoke_now') == 'no'
                and cleaned_data.get('years_smoked')):
            raise forms.ValidationError('Subject quit smoking. DO NOT give'
                                        ' any details about smoking NOW.')

        if (cleaned_data.get('smoke_now') == 'no'
                and not cleaned_data.get('cigarette_smoked')):
            raise forms.ValidationError(
                'Subject used to smoke but quit. How many '
                'cigarettes did he/she smoke per day?')
        if (cleaned_data.get('smoke_now') == 'no'
                and not cleaned_data.get('when_quit')):
            raise forms.ValidationError(
                'Subject used to smoke but quit. When did he/she quit?')
        if (cleaned_data.get('smoke_now') == 'no'
                and not cleaned_data.get('years_smoked_before')):
            raise forms.ValidationError(
                'Subject used to smoke but quit. For how many years '
                'did he/she smoke before he/she quit?')

        return cleaned_data

    class Meta:
        model = BaseRiskAssessmentSmoking
        fields = '__all__'
