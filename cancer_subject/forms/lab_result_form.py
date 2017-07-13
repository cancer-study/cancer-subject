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
        fields = '__all__'


# LabResultHeightWeight
class LabResultHeightWeightForm (SubjectModelFormMixin):

    class Meta:
        model = LabResultHeightWeight
        fields = '__all__'


# LabResultHiv
class LabResultHivForm (SubjectModelFormMixin):

    class Meta:
        model = LabResultHiv
        fields = '__all__'


# LabResultCd4
class LabResultCd4Form (SubjectModelFormMixin):

    class Meta:
        model = LabResultCd4
        fields = '__all__'


# LabResultViralload
class LabResultViralloadForm (SubjectModelFormMixin):

    class Meta:
        model = LabResultViralload
        fields = '__all__'


# LabResultHaematology
class LabResultHaematologyForm (SubjectModelFormMixin):

    class Meta:
        model = LabResultHaematology
        fields = '__all__'


# LabResultChemistry
class LabResultChemistryForm (SubjectModelFormMixin):

    class Meta:
        model = LabResultChemistry
        fields = '__all__'


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
        fields = '__all__'
