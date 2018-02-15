from django import forms


from edc_constants.constants import YES, NO

from ..models import CancerDiagnosis
from .form_mixins import SubjectModelFormMixin


# CancerDiagnosis
class CancerDiagnosisForm (SubjectModelFormMixin):

    def clean(self):
        cleaned_data = self.cleaned_data
        # validating results_to_record
#         if cleaned_data.get('results_to_record')[0].name == 'Haematology':
#             raise forms.ValidationError('You should now '
# 'fill out the LabResult:Haematology form')

    # validating cancer_diagnosis
        if cleaned_data['diagnosis'] == YES and not cleaned_data['cancer_category']:
            raise forms.ValidationError(
                'If patient is diagnosed with cancer, provide cancer_case')
#         if cleaned_data['diagnosis'] == YES and not cleaned_data['symptom_prompt']:
#             raise forms.ValidationError('If patient is diagnosed with cancer, '
# 'which symptom led to diagnosis of cancer')
#
#         if cleaned_data['symptom_prompt'] and not '
# 'cleaned_data['symptom_first_noticed']:
#             raise forms.ValidationError('If symptom was noted, '
# 'provide date when symptom was first noticed')
#         if cleaned_data['symptom_prompt'] and not '
# 'cleaned_data['first_evaluation']:
#             raise forms.ValidationError('If symptom was noted, '
# 'provide date when patient received evaluation')

        if (cleaned_data['diagnosis'] == YES
            and not cleaned_data['date_diagnosed']
                and not cleaned_data['diagnosis_basis']):
            raise forms.ValidationError(
                'A cancer diagnosis was made, please provide date of '
                'cancer diagnosis and basis for diagnosis')
        if (cleaned_data['date_diagnosed'] != ''
            and not cleaned_data['diagnosis_word']
                and not cleaned_data['cancer_site']):
            raise forms.ValidationError(
                'Cancer diagnosis date has been given, please provide'
                ' cancer diagnosis in WORDS and the cancer site code')
#         if not cleaned_data['onco_number']
# and not cleaned_data['pathology_number'] and not cleaned_data['pm_number']:
#             raise forms.ValidationError('Please provide either an oncology,'
# ' pathology or pm number. Please correct.')
        if cleaned_data.get('diagnosis') == NO:
            raise forms.ValidationError(
                'AT enrollment you mentioned that a cancer diagnosis '
                'was documented, so answer to whether a cancer diagnosis '
                'has been made should be YES. please correct!')
        cleaned_data = super(CancerDiagnosisForm, self).clean()
        return cleaned_data

    class Meta:
        model = CancerDiagnosis
        fields = '__all__'
