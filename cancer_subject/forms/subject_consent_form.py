from django import forms
from edc_consent.modelform_mixins import ConsentModelFormMixin

from cancer_subject_validations.form_validators import SubjectConsentFormValidation

from ..choices import ID_TYPE
from ..models import SubjectConsent
from .form_mixins import SubjectModelFormMixin


class SubjectConsentForm(ConsentModelFormMixin, SubjectModelFormMixin,
                         forms.ModelForm):

    form_validator_cls = SubjectConsentFormValidation

    identity_type = forms.CharField(
        label='What type of identity number is this?',
        widget=forms.RadioSelect(choices=list(ID_TYPE)))

    class Meta:
        model = SubjectConsent
        fields = '__all__'
