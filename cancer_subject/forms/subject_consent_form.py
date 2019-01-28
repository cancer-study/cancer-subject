from django import forms

from edc_consent.modelform_mixins import ConsentModelFormMixin
from ..choices import COMMUNITY, ID_TYPE
from ..models import SubjectConsent


class SubjectConsentForm(ConsentModelFormMixin, forms.ModelForm):

    identity_type = forms.CharField(
        label='What type of identity number is this?',
        widget=forms.RadioSelect(choices=list(ID_TYPE)))

    study_site = forms.ChoiceField(
        label='Study site',
        choices=COMMUNITY,
        help_text="",
        widget=forms.RadioSelect())

    class Meta:
        model = SubjectConsent
        fields = '__all__'
