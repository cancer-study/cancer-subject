from django import forms

from .modelform_mixin import SubjectModelFormMixin

from ..models import (
    LabResult, LabResultHeightWeight, LabResultHiv,
    LabResultCd4, LabResultViralload, LabResultHaematology, LabResultChemistry,
    LabResultTb)


# LabResult
class LabResultForm (SubjectModelFormMixin):

    class Meta:
        model = LabResult


# LabResultHeightWeight
class LabResultHeightWeightForm (SubjectModelFormMixin):

    class Meta:
        model = LabResultHeightWeight


# LabResultHiv
class LabResultHivForm (SubjectModelFormMixin):

    class Meta:
        model = LabResultHiv


# LabResultCd4
class LabResultCd4Form (SubjectModelFormMixin):

    class Meta:
        model = LabResultCd4


# LabResultViralload
class LabResultViralloadForm (SubjectModelFormMixin):

    class Meta:
        model = LabResultViralload


# LabResultHaematology
class LabResultHaematologyForm (SubjectModelFormMixin):

    class Meta:
        model = LabResultHaematology


# LabResultChemistry
class LabResultChemistryForm (SubjectModelFormMixin):

    class Meta:
        model = LabResultChemistry


# LabResultTb
class LabResultTbForm (SubjectModelFormMixin):

    def clean(self):
        cleaned_data = self.cleaned_data
        if cleaned_data['tb_treatment'] == 'Yes, isoniazid preventative therapy (IPT)' and not cleaned_data['tb_treatment_start']:
            raise forms.ValidationError('If participant is receiving any kind of treatment, when did this treatment begin')
        if cleaned_data['tb_treatment'] == 'Yes, combination anti-tuberculosis treatment (ATT)' and not cleaned_data['tb_treatment_start']:
            raise forms.ValidationError('If participant is receiving any kind of treatment, when did this treatment begin')
        cleaned_data = super(LabResultTbForm, self).clean()
        return cleaned_data

    class Meta:
        model = LabResultTb
