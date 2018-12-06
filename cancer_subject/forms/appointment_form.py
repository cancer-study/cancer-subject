from django import forms
from edc_appointment.form_validators import AppointmentFormValidator
from edc_appointment.models.appointment import Appointment

from ..choices import APPOINTMENT_REASON


class AppointmentForm(AppointmentFormValidator, forms.ModelForm):

    appt_reason = forms.ChoiceField(
        label='Reason for appointment:',
        choices=APPOINTMENT_REASON,
        widget=forms.RadioSelect)

    def validate_appt_reason(self):
        pass

    class Meta:
        model = Appointment
        fields = '__all__'
