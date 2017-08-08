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

#     def validate_data_fields(self):
#         screening_identifier = self.cleaned_data.get(
#             'screening_identifier')
#         first_name = self.cleaned_data.get('first_name')
#         initials = self.cleaned_data.get('initials')
#
#         try:
#             subject_eligibility = SubjectEligibility.objects.get(
#                 screening_identifier=screening_identifier)
#         except SubjectEligibility.DoesNotExist:
#             raise forms.ValidationError(
#                 f'Please complete \'{SubjectEligibility._meta.verbose_name}\' first.')
#         else:
#             if subject_eligibility.first_name != first_name:
#                 raise forms.ValidationError({
#                     'first_name': f'Does not match {SubjectEligibility._meta.verbose_name}'})
#             if subject_eligibility.initials != initials:
#                 raise forms.ValidationError({
#                     'initials': f'Does not match {SubjectEligibility._meta.verbose_name}'})
#
#     study_site = forms.ChoiceField(
#         label='Study site',
#         choices=COMMUNITIES,
#         help_text="",
#         widget=forms.RadioSelect())
#
#     class Meta:
#         model = SubjectConsent
#         fields = '__all__'

    class Meta:
        model = SubjectConsent
        fields = '__all__'
