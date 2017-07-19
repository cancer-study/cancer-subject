from django import forms


from cancer_subject_validations.form_validators import (
    SubjectConsentFormValidation)

from ..models import SubjectConsent


class SubjectConsentForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data = SubjectConsentFormValidation(
            cleaned_data=cleaned_data).clean()
        return cleaned_data

    class Meta:
        model = SubjectConsent
        fields = '__all__'
