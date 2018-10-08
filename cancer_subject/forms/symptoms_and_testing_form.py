from django import forms
from edc_constants.constants import YES, NO

from ..models import SymptomsAndTesting
from .form_mixins import SubjectModelFormMixin


class SymptomsAndTestingForm (SubjectModelFormMixin):

    def clean(self):
        cleaned_data = self.cleaned_data
        if (cleaned_data.get('hiv_tested') == YES
                and not cleaned_data.get('hiv_test_result')):
            raise forms.ValidationError(
                'If subject has been tested for HIV, what was the test result')

        if (cleaned_data['hiv_test_result'] == 'NEG'
                and not cleaned_data['neg_date']):
            raise forms.ValidationError('If most recent HIV test result is '
                                        'negative, please provide date of last'
                                        ' negative result')
        # blocking user from providing wrong date
        if (cleaned_data['hiv_test_result'] == 'NEG'
                and cleaned_data['pos_date']):
            raise forms.ValidationError(
                'Subject is NEG, you cannot answer POS date')

        if (cleaned_data['hiv_test_result'] == 'POS'
                and not cleaned_data['pos_date']):
            raise forms.ValidationError('If most recent HIV test result is '
                                        'positive, please  provide date of '
                                        'last positive result')
        # blocking user from providing wrong date
        if (cleaned_data['hiv_test_result'] == 'POS'
                and cleaned_data['neg_date']):
            raise forms.ValidationError(
                'Subject is POS, you cannot answer NEG date')

        if cleaned_data.get('hiv_tested') == NO and cleaned_data.get(
                'hiv_test_result') and cleaned_data.get('pos_date'):
            raise forms.ValidationError('If subject has NEVER tested for HIV,'
                                        ' do not key any result details')

        if (cleaned_data['arv_art_therapy'] == YES
                and not cleaned_data['arv_art_start_date']):
            raise forms.ValidationError(
                'If patient has taken HAART, provide the start date')

        if (cleaned_data['arv_art_therapy'] == YES
                and not cleaned_data['arv_art_now']):
            raise forms.ValidationError(
                'If patient took HAART before, are they taking HAART even now')

        if (cleaned_data['arv_art_therapy'] == NO
                and cleaned_data['arv_art_start_date']):
            raise forms.ValidationError('If patient has NEVER started HAART.'
                                        ' You CANNOT provide a start date')

        if (cleaned_data['arv_art_therapy'] == NO
                and cleaned_data['arv_art_now'] == YES):
            raise forms.ValidationError('Patient has NEVER taken HAART. '
                                        'They CANNOT be taking HAART NOW.')

        if (cleaned_data['arv_art_therapy'] == NO
                and cleaned_data['art_art_stop_date']):
            raise forms.ValidationError('Patient has NEVER taken HAART.'
                                        ' You CANNOT provide a stop date.')

        if (cleaned_data['arv_art_now'] == NO
                and not cleaned_data['art_art_stop_date']):
            raise forms.ValidationError(
                'Patient has STOPPED taking HAART. Please provide STOP DATE')

        if (cleaned_data['arv_art_now'] == YES
                and cleaned_data['art_art_stop_date']):
            raise forms.ValidationError('You CANNOT give a stop date '
                                        'because patient is taking HAART NOW')

        if cleaned_data.get("facility_first_seen") == '00-0-00':
            if not cleaned_data.get("facility_first_seen_other"):
                raise forms.ValidationError('if facility is 00-0-00, please '
                                            'provide the name of the facility')

        cleaned_data = super(SymptomsAndTestingForm, self).clean()
        return cleaned_data

    class Meta:
        model = SymptomsAndTesting
        fields = '__all__'
