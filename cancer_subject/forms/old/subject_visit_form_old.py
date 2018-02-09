from django import forms
from django.contrib.admin.widgets import AdminRadioSelect, AdminRadioFieldRenderer

from edc.subject.consent.forms import BaseConsentedModelForm
from ...cancer_subject.choices import VISIT_INFO_SOURCE
from ..models import SubjectVisit


class SubjectVisitForm (BaseConsentedModelForm):

    """Based on model visit.

    Attributes reason and info_source override those from the base model so that
    the choices can be custom for this app.

    """

    reason = forms.ChoiceField(
        label='Reason for visit',
        choices=SubjectVisit().get_visit_reason_choices(),
        help_text="If 'unscheduled', information is usually reported at the next scheduled visit, but exceptions may arise",
        widget=AdminRadioSelect(renderer=AdminRadioFieldRenderer),
        )
    info_source = forms.ChoiceField(
        label='Source of information',
        choices=[choice for choice in VISIT_INFO_SOURCE],
        widget=AdminRadioSelect(renderer=AdminRadioFieldRenderer),
        )

    def clean(self):

        cleaned_data = self.cleaned_data

        """validate data"""
        if cleaned_data['reason'] == 'missed' and not cleaned_data['reason_missed']:
            raise forms.ValidationError('Please provide the reason the scheduled visit was missed')
        if cleaned_data['reason'] != 'missed' and cleaned_data['reason_missed']:
            raise forms.ValidationError("Reason for visit is NOT 'missed' but you provided a reason missed. Please correct.")
        if cleaned_data['info_source'] == 'OTHER' and not cleaned_data['info_source_other']:
            raise forms.ValidationError("Source of information is 'OTHER', please provide details below your choice")

        cleaned_data = super(SubjectVisitForm, self).clean()

        return cleaned_data

    class Meta:
        model = SubjectVisit
