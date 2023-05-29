from django import forms
from edc_consent import ConsentObjectDoesNotExist
from edc_consent.consent_helper import ConsentHelper
from edc_consent.modelform_mixins import ConsentModelFormMixin
from edc_consent.site_consents import site_consents, SiteConsentError

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

    def update_consent(self):
        consent_datetime = self.cleaned_data.get(
            'consent_datetime') or self.instance.consent_datetime
        if consent_datetime:
            if self.consent_config.updates_versions:
                ConsentHelper(
                    model_cls=self._meta.model,
                    update_previous=False,
                    **self.cleaned_data)

    @property
    def consent_config(self):
        cleaned_data = self.cleaned_data
        try:
            consent_config = site_consents.get_consent(
                model=self._meta.model._meta.label_lower,
                report_datetime=cleaned_data.get(
                    'consent_datetime') or self.instance.consent_datetime,
                consent_model=self._meta.model._meta.label_lower,
                consent_group=self._meta.model._meta.consent_group,
                version=self.instance.version
            )
        except (ConsentObjectDoesNotExist, SiteConsentError) as e:
            raise forms.ValidationError(e)
        return consent_config

    class Meta:
        model = SubjectConsent
        fields = '__all__'
