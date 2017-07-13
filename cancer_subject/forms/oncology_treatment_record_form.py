from django import forms

from .modelform_mixin import SubjectModelFormMixin
from ..models import OncologyTreatmentRecord, OTRChemo, OTRRadiation, OTRSurgical
from edc_constants.constants import YES, NO


class OncologyTreatmentRecordForm (SubjectModelFormMixin):

    class Meta:
        model = OncologyTreatmentRecord


class OTRChemoForm (SubjectModelFormMixin):

    def clean(self):
        cleaned_data = self.cleaned_data
        if cleaned_data['chemo_delays'] == YES and not cleaned_data['why_delayed']:
            raise forms.ValidationError('If doses have been delayed, what is the reason for the delay')
        if cleaned_data['chemo_delays'] == NO and cleaned_data['why_delayed']:
            raise forms.ValidationError('NO doses where delayed, do not provide any delay reasons')
        if cleaned_data['chemo_reduced'] == YES and not cleaned_data['why_reduced']:
            raise forms.ValidationError('If doses have been reduced, why were the doses reduced')
        if cleaned_data['chemo_reduced'] == NO and cleaned_data['why_reduced']:
            raise forms.ValidationError('NO doses reduced, do not provide any reasons for reducing dose')
        cleaned_data = super(OTRChemoForm, self).clean()
        return cleaned_data

    class Meta:
        model = OTRChemo


class OTRRadiationForm (SubjectModelFormMixin):
    def clean(self):
        cleaned_data = self.cleaned_data

    # validating radiation
        if cleaned_data['radiation_details'] == 'Yes' and not cleaned_data['concomitant'] and not cleaned_data['amount_radiation']:
            raise forms.ValidationError('If patient radiation details are available, please provide remaining details on form')
        cleaned_data = super(OTRRadiationForm, self).clean()
        return cleaned_data

    class Meta:
        model = OTRRadiation


class OTRSurgicalForm (SubjectModelFormMixin):

    class Meta:
        model = OTRSurgical
