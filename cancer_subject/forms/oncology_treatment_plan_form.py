from django import forms

from edc_constants.constants import YES, NO

from .modelform_mixin import SubjectModelFormMixin
from ..models import OncologyTreatmentPlan


# OncologyTreatmentPlan
class OncologyTreatmentPlanForm (SubjectModelFormMixin):

    def clean(self):
        cleaned_data = self.cleaned_data

        if (cleaned_data.get('treatment_plan') == YES
            and not cleaned_data.get('chemotherapy')
            and not cleaned_data.get('radiation_plan')
                and not cleaned_data.get('surgical_plan')):
            raise forms.ValidationError(
                'If treatment is planned, please provide '
                'information for chemotherapy, radiation & surgical')
        if (cleaned_data.get('chemotherapy') == YES
                and not cleaned_data.get('chemo_intent')):
            raise forms.ValidationError(
                'If chemotherapy is planned, what is the intent of giving it?')
        if (cleaned_data.get('chemotherapy') == NO
                and cleaned_data.get('chemo_intent')):
            raise forms.ValidationError(
                'NO chemo intent should be provided. CHEMO is NOT PLANNED')
        if (cleaned_data.get('surgical_plan') == YES
                and not cleaned_data.get('planned_operation')):
            raise forms.ValidationError(
                'If surgery is planned, describe the planned operation')
        if (cleaned_data.get('surgical_plan') == NO
                and cleaned_data.get('planned_operation')):
            raise forms.ValidationError(
                'NO surgery planned. Do not describe planned operation')
        cleaned_data = super(OncologyTreatmentPlanForm, self).clean()
        return cleaned_data

    class Meta:
        model = OncologyTreatmentPlan
        fields = '__all__'
