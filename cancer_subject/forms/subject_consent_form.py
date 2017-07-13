from django import forms

from edc_constants.choices import YES_NO

from ..models import SubjectConsent


class SubjectConsentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['guardian_name'].label = (
            'Guardian\'s Last and first name (for patients with Abnormal mental status)')
        self.fields['guardian_name'].help_text = (
            'Required only if subject is unconscious or has an abnormal mental '
            'status. Format is \'LASTNAME, FIRSTNAME\'. All uppercase separated '
            'by a comma then followed by a space.')

    store_genetic_samples = forms.ChoiceField(
        label=('Does the subject agree that a portion of the blood sample '
               'that is taken be stored for genetic analysis?'),
        choices=YES_NO,
        widget=forms.RadioSelect)

    def clean(self):
        cleaned_data = super().clean()
#         cleaned_data = SubjectConsentFormValidator(
#             cleaned_data=cleaned_data).clean()
        return cleaned_data

    class Meta:
        model = SubjectConsent
        fields = '__all__'
