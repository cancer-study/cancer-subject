from django import forms
from edc_appointment.form_validators import AppointmentFormValidator as BaseAppointmentFormValidator
from edc_appointment.models.appointment import Appointment
from edc_base.sites.forms import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin

from ..choices import APPOINTMENT_REASON


class AppointmentFormValidator(BaseAppointmentFormValidator):

    def validate_appt_reason(self):
        print('>>>>>>>>>>>>>>>>')
        pass


class AppointmentForm(SiteModelFormMixin, FormValidatorMixin, forms.ModelForm):

    appt_reason = forms.ChoiceField(
        label='Reason for appointment:',
        choices=APPOINTMENT_REASON,
        widget=forms.RadioSelect)

    form_validator_cls = AppointmentFormValidator

    class Meta:
        model = Appointment
        fields = '__all__'
