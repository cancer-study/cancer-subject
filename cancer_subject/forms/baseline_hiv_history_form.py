from django import forms
from edc_constants.constants import YES, NO

from ..models import BaselineHIVHistory
from .form_mixins import SubjectModelFormMixin


# BaselineHIVHistory
class BaselineHIVHistoryForm (SubjectModelFormMixin):
    def clean(self):
        cleaned_data = self.cleaned_data
        if (cleaned_data.get('has_cd4') == YES
                and not cleaned_data.get('cd4_result')):
            raise forms.ValidationError('If CD4 results are available, '
                                        'what is the value of the result?')
        if (cleaned_data.get('cd4_result')
                and not cleaned_data.get('cd4_drawn_date')):
            raise forms.ValidationError(
                'You have provided the value of the CD4 result, '
                'what is the CD4 drawn date?')
        if (cleaned_data.get('has_cd4') == NO
                and cleaned_data.get('cd4_result')):
            raise forms.ValidationError('NO CD4 results are available, '
                                        'DO NOT GIVE a CD4 result value?')
        if (cleaned_data.get('has_cd4') == NO
                and cleaned_data.get('cd4_drawn_date')):
            raise forms.ValidationError(
                'NO CD4 results are available, DO NOT GIVE a CD4 result date?')

        if (cleaned_data.get('has_prior_cd4') == YES
                and not cleaned_data.get('nadir_cd4')):
            raise forms.ValidationError(
                'If a prior CD4 result is available, please provide '
                'the value of the LOWEST CD4 result')
        if (cleaned_data.get('nadir_cd4')
                and not cleaned_data.get('nadir_cd4_drawn_date')):
            raise forms.ValidationError(
                'You have provided the lowest CD4 result. Please '
                'provide the LOWEST CD4 result date')
        if (cleaned_data.get('has_prior_cd4') == NO
                and cleaned_data.get('nadir_cd4')):
            raise forms.ValidationError(
                'NO prior CD4 result is available, DO NOT provide '
                'the LOWEST CD4 result value')
        if (cleaned_data.get('has_prior_cd4') == NO
                and cleaned_data.get('nadir_cd4')):
            raise forms.ValidationError(
                'NO prior CD4 result is available, DO NOT provide'
                ' the LOWEST CD4 result date')

        # CD4 result values validations
        if cleaned_data.get('nadir_cd4') > cleaned_data.get('cd4_result'):
            raise forms.ValidationError('The LOWEST CD4 CANNOT be GREATER '
                                        'than the most RECENT CD4 result')
        if cleaned_data.get('cd4_result') < cleaned_data.get('nadir_cd4'):
            raise forms.ValidationError('The most RECENT CD4 CANNOT be '
                                        'LESS than the LOWEST CD4 result')

        if (cleaned_data.get('has_vl') == YES
                and not cleaned_data.get('vl_result')):
            raise forms.ValidationError('If VL results are available, '
                                        'What is the value of the result?')
        if (cleaned_data.get('vl_result')
                and not cleaned_data.get('vl_drawn_date')):
            raise forms.ValidationError('You have provided the VL result '
                                        'value, when was the draw date?')

        if cleaned_data.get('has_vl') == NO and cleaned_data.get('vl_result'):
            raise forms.ValidationError(
                'NO VL results. DO NOT provide a VL result value')
        if (cleaned_data.get('has_vl') == NO
                and cleaned_data.get('vl_drawn_date')):
            raise forms.ValidationError(
                'NO VL results. DO NOT provide a VL result date')
        cleaned_data = super(BaselineHIVHistoryForm, self).clean()
        return cleaned_data

    class Meta:
        model = BaselineHIVHistory
        fields = '__all__'
