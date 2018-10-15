from django import forms

from ..choices import COMMUNITY, ID_TYPE
from ..models import SubjectConsent


class SubjectConsentForm(forms.ModelForm):

    screening_identifier = forms.CharField(
        label='Screening identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    identity_type = forms.CharField(
        label='What type of identity number is this?',
        widget=forms.RadioSelect(choices=list(ID_TYPE)))

    study_site = forms.ChoiceField(
        label='Study site',
        choices=COMMUNITY,
        help_text="",
        widget=forms.RadioSelect())

    def clean(self):
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>", self.errors.keys())

    class Meta:
        model = SubjectConsent
        fields = '__all__'
