from django import forms

from ..choices import APPOINTMENT_REASON
# from edc_appointment.model_mixins import AppointmentModelMixin

from ..models import Appointment


class AppointmentForm(forms.ModelForm):

    appt_reason = forms.ChoiceField(
        label='Reason for appointment:',
        choices=APPOINTMENT_REASON,
        widget=forms.RadioSelect)

    class Meta:
        model = Appointment
        fields = '__all__'
