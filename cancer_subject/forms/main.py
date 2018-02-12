from django import forms

from .modelform_mixin import SubjectModelFormMixin
from ..models import (
    ActivityAndFunctioning, CancerDiagnosis, ChemoMedPlan, ChemoMedRecord,
    HaartRecord, HaartMedRecord, OncologyTreatmentPlan,
    Referral, TreatmentResponse, SymptomsAndTesting,
    OncologyTreatmentCompleted, CurrentSymptoms)

from edc_constants.constants import YES, NO


# ActivityAndFunctioning
class ActivityAndFunctioningForm (SubjectModelFormMixin):

    class Meta:
        model = ActivityAndFunctioning
        fields = '__all__'


# CancerDiagnosis
class CancerDiagnosisForm (SubjectModelFormMixin):

    def clean(self):
        cleaned_data = self.cleaned_data
        # validating results_to_record
#         if cleaned_data.get('results_to_record')[0].name == 'Haematology':
#             raise forms.ValidationError('You should now fill out the LabResult:Haematology form')

    # validating cancer_diagnosis
        if cleaned_data['diagnosis'] == YES and not cleaned_data['cancer_category']:
            raise forms.ValidationError(
                'If patient is diagnosed with cancer, provide cancer_case')
#         if cleaned_data['diagnosis'] == YES and not cleaned_data['symptom_prompt']:
#             raise forms.ValidationError('If patient is diagnosed with cancer, which symptom led to diagnosis of cancer')
#
#         if cleaned_data['symptom_prompt'] and not cleaned_data['symptom_first_noticed']:
#             raise forms.ValidationError('If symptom was noted, provide date when symptom was first noticed')
#         if cleaned_data['symptom_prompt'] and not cleaned_data['first_evaluation']:
#             raise forms.ValidationError('If symptom was noted, provide date when patient received evaluation')

        if cleaned_data['diagnosis'] == YES and not cleaned_data['date_diagnosed'] and not cleaned_data['diagnosis_basis']:
            raise forms.ValidationError(
                'A cancer diagnosis was made, please provide date of cancer diagnosis and basis for diagnosis')
        if cleaned_data['date_diagnosed'] != '' and not cleaned_data['diagnosis_word'] and not cleaned_data['cancer_site']:
            raise forms.ValidationError(
                'Cancer diagnosis date has been given, please provide cancer diagnosis in WORDS and the cancer site code')
#         if not cleaned_data['onco_number'] and not cleaned_data['pathology_number'] and not cleaned_data['pm_number']:
#             raise forms.ValidationError('Please provide either an oncology, pathology or pm number. Please correct.')
        if cleaned_data.get('diagnosis') == NO:
            raise forms.ValidationError('AT enrollment you mentioned that a cancer diagnosis '
                                        'was documented, so answer to whether a cancer diagnosis '
                                        'has been made should be YES. please correct!')
        cleaned_data = super(CancerDiagnosisForm, self).clean()
        return cleaned_data

    class Meta:
        model = CancerDiagnosis
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


class OncologyTreatmentCompletedForm (SubjectModelFormMixin):

    def clean(self):
        cleaned_data = self.cleaned_data

        if cleaned_data.get('patient_had_chemo') == YES and not cleaned_data.get('treatment_detail'):
            raise forms.ValidationError(
                'Treatment is planned. Please provide details of the treatment')
        if cleaned_data.get('patient_had_radiation') == YES and not cleaned_data.get('treatment_detail'):
            raise forms.ValidationError(
                'Treatment is planned. Please provide details of the treatment')
        if cleaned_data.get('patient_had_surgery') == YES and not cleaned_data.get('treatment_detail'):
            raise forms.ValidationError(
                'Treatment is planned. Please provide details of the treatment')

        cleaned_data = super(OncologyTreatmentCompletedForm, self).clean()

        return cleaned_data

    class Meta:
        model = OncologyTreatmentCompleted
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
