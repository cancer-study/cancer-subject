from django import forms

from .modelform_mixin import SubjectModelFormMixin
from ..models import (ActivityAndFunctioning, ChemoMedPlan, ChemoMedRecord,
                      HaartRecord, HaartMedRecord, OncologyTreatmentPlan,
                      CurrentSymptoms)

from edc_constants.constants import YES, NO


# ActivityAndFunctioning
class ActivityAndFunctioningForm (SubjectModelFormMixin):

    class Meta:
        model = ActivityAndFunctioning
        fields = '__all__'


# ChemoMedPlan
class ChemoMedPlanForm (SubjectModelFormMixin):

    class Meta:
        model = ChemoMedPlan
        fields = '__all__'


# ChemoMedRecord
class ChemoMedRecordForm (SubjectModelFormMixin):

    class Meta:
        model = ChemoMedRecord
        fields = '__all__'


# HaartRecord
class HaartRecordForm (SubjectModelFormMixin):

    class Meta:
        model = HaartRecord
        fields = '__all__'


# HaartMedRecord
class HaartMedRecordForm (SubjectModelFormMixin):

    class Meta:
        model = HaartMedRecord
        fields = '__all__'


# OncologyTreatmentPlan
class OncologyTreatmentPlanForm (SubjectModelFormMixin):

    def clean(self):
        cleaned_data = self.cleaned_data

        if cleaned_data.get('treatment_plan') == YES and not cleaned_data.get('chemotherapy') and not cleaned_data.get('radiation_plan') and not cleaned_data.get('surgical_plan'):
            raise forms.ValidationError(
                'If treatment is planned, please provide information for chemotherapy, radiation & surgical')
        if cleaned_data.get('chemotherapy') == YES and not cleaned_data.get('chemo_intent'):
            raise forms.ValidationError(
                'If chemotherapy is planned, what is the intent of giving it?')
        if cleaned_data.get('chemotherapy') == NO and cleaned_data.get('chemo_intent'):
            raise forms.ValidationError(
                'NO chemo intent should be provided. CHEMO is NOT PLANNED')
        if cleaned_data.get('surgical_plan') == YES and not cleaned_data.get('planned_operation'):
            raise forms.ValidationError(
                'If surgery is planned, describe the planned operation')
        if cleaned_data.get('surgical_plan') == NO and cleaned_data.get('planned_operation'):
            raise forms.ValidationError(
                'NO surgery planned. Do not describe planned operation')
        cleaned_data = super(OncologyTreatmentPlanForm, self).clean()
        return cleaned_data

    class Meta:
        model = OncologyTreatmentPlan
        fields = '__all__'


class CurrentSymptomsForm (SubjectModelFormMixin):

    def clean(self):
        cleaned_data = self.cleaned_data

        if cleaned_data.get('any_worry') == YES and not cleaned_data.get('symptom_desc'):
            raise forms.ValidationError(
                'If patient is worried, please provide a description of their symptom')
        if cleaned_data.get('any_worry') == YES and not cleaned_data.get('patient_own_remedy'):
            raise forms.ValidationError(
                'If patient is worried, has the patient tried to do anything about it?')
        if cleaned_data.get('any_worry') == YES and not cleaned_data.get('severity'):
            raise forms.ValidationError('How severe is/are the symptom(s)?')
#         if cleaned_data.get('ra_advice') and not cleaned_data.get('outcome_update'):
#             raise forms.ValidationError('If RA has provided advice/help, what is the outcome or update?')

        cleaned_data = super(CurrentSymptomsForm, self).clean()

        return cleaned_data

    class Meta:
        model = CurrentSymptoms
        fields = '__all__'
