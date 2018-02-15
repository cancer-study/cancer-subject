from django import forms

from edc_constants.constants import YES

from ..models import CurrentSymptoms
from .form_mixins import SubjectModelFormMixin


class CurrentSymptomsForm (SubjectModelFormMixin):

    def clean(self):
        cleaned_data = self.cleaned_data

        if (cleaned_data.get('any_worry') == YES
                and not cleaned_data.get('symptom_desc')):
            raise forms.ValidationError('If patient is worried, please'
                                        ' provide a description of their symptom')
        if (cleaned_data.get('any_worry') == YES
                and not cleaned_data.get('patient_own_remedy')):
            raise forms.ValidationError(
                'If patient is worried, has the patient '
                'tried to do anything about it?')
        if (cleaned_data.get('any_worry') == YES
                and not cleaned_data.get('severity')):
            raise forms.ValidationError('How severe is/are the symptom(s)?')
#         if cleaned_data.get('ra_advice') and not cleaned_data.get('outcome_update'):
#             raise forms.ValidationError('If RA has provided advice/help, what is the outcome or update?')

        cleaned_data = super(CurrentSymptomsForm, self).clean()

        return cleaned_data

    class Meta:
        model = CurrentSymptoms
        fields = '__all__'
