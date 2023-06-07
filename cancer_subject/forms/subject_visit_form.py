from django import forms
from edc_base.sites import SiteModelFormMixin
from edc_constants.constants import OTHER
from edc_form_validators import FormValidatorMixin
from edc_form_validators.base_form_validator import INVALID_ERROR
from edc_visit_tracking.constants import UNSCHEDULED, MISSED_VISIT
from edc_visit_tracking.form_validators import \
    VisitFormValidator as BaseVisitFormValidator
from django.apps import apps as django_apps

from ..models import SubjectVisit


class VisitFormValidator(BaseVisitFormValidator):
    death_model = 'cancer_prn.deathreport'

    def clean(self):
        super().clean()
        self.validate_no_death_obj()
        self.validate_no_death_visit()

    def validate_no_death_obj(self):
        """Validates that the participant associated with `subject_identifier` has
        not already been marked as deceased in the `death_cls` model. Raises a
        `forms.ValidationError` if the participant is deceased.
        """
        subject_identifier = self.cleaned_data.get('subject_identifier')
        self.death_cls = django_apps.get_model(self.death_model)
        try:
            self.death_cls.objects.get(
                subject_identifier=subject_identifier)
        except self.death_cls.DoesNotExist:
            # if no existing death object found, pass validation
            return

        if self.instance is not None and self.instance.pk is not None:
            # if updating an existing instance, ignore the found death object
            return

        raise forms.ValidationError('You cannot start a new appointment if the '
                                    'participant is dead!')

    def validate_no_death_visit(self):
        """Validates if a new visit can be started for a participant.
        Raises ValidationError if the participant is dead.

        Args:
            self: instance of the form
        """
        subject_identifier = self.cleaned_data.get('subject_identifier')
        death_visits = SubjectVisit.objects.filter(
            reason='Death', subject_identifier=subject_identifier)
        if not hasattr(self.instance, 'pk') and death_visits:
            raise forms.ValidationError('You cannot start a new visit if the '
                                        'participant is dead!')

    def validate_visit_code_sequence_and_reason(self):
        appointment = self.cleaned_data.get('appointment')
        reason = self.cleaned_data.get('reason')
        if appointment:
            if (appointment.visit_code not in ['1000']
                    and reason == UNSCHEDULED):
                raise forms.ValidationError({
                    'reason': 'Invalid. This is not an unscheduled visit'},
                    code=INVALID_ERROR)

    def validate_required_fields(self):

        self.required_if(
            MISSED_VISIT,
            field='reason',
            field_required='reason_missed')

        self.required_if(
            'Unscheduled visit/contact',
            field='reason',
            field_required='reason_unscheduled')

        self.required_if(
            OTHER,
            field='info_source',
            field_required='info_source_other')

        self.required_if(
            OTHER,
            field='reason_unscheduled',
            field_required='reason_unscheduled_other')


class SubjectVisitForm(
    SiteModelFormMixin, FormValidatorMixin, forms.ModelForm):
    form_validator_cls = VisitFormValidator

    class Meta:
        model = SubjectVisit
        fields = '__all__'
