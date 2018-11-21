from django import forms
from edc_appointment.models.appointment import Appointment

from ..choices import APPOINTMENT_REASON


class AppointmentForm(forms.ModelForm):

    appt_reason = forms.ChoiceField(
        label='Reason for appointment:',
        choices=APPOINTMENT_REASON,
        widget=forms.RadioSelect)

    class Meta:
        model = Appointment
        fields = '__all__'
