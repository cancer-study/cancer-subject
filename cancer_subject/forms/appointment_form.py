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
        appt_type = self.cleaned_data.get('appt_type')
        if (appt_reason and self.instance.visit_code != '1000'
                and appt_reason != UNSCHEDULED_APPT):
            raise forms.ValidationError({
                'appt_reason': f'Expected {UNSCHEDULED_APPT.title()}'})
        if (appt_type in ['telephone', 'clinic', 'home']
                and self.instance.visit_code == '1000'):
            raise forms.ValidationError({
                'appt_type': f'Only follow up appointments can be done via telephone, '
                'at home or clinic.'})


class AppointmentForm(SiteModelFormMixin, FormValidatorMixin, forms.ModelForm):
    """Note, the appointment is only changed, never added,
    through this form.
    """

    form_validator_cls = AppointmentFormValidator

    class Meta:
        model = Appointment
        fields = '__all__'
