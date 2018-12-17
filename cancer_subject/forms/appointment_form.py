from django import forms
from edc_appointment.constants import UNSCHEDULED_APPT
from edc_appointment.form_validators import (
    AppointmentFormValidator as BaseAppointmentFormValidator)
from edc_base.sites.forms import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin

from ..models import Appointment


class AppointmentFormValidator(BaseAppointmentFormValidator):

    def validate_appt_reason(self):
        """Raises if visit_code_sequence is not 0 and appt_reason
        is not UNSCHEDULED_APPT.
        """
        appt_reason = self.cleaned_data.get('appt_reason')
        if (appt_reason and self.instance.visit_code_sequence
                and appt_reason != UNSCHEDULED_APPT):
            raise forms.ValidationError({
                'appt_reason': f'Expected {UNSCHEDULED_APPT.title()}'})


class AppointmentForm(SiteModelFormMixin, FormValidatorMixin, forms.ModelForm):
    """Note, the appointment is only changed, never added,
    through this form.
    """

    form_validator_cls = AppointmentFormValidator

    class Meta:
        model = Appointment
        fields = '__all__'
