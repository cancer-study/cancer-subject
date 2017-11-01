from django import forms

from cancer_subject.choices.main import APPOINTMENT_REASON
from edc_appointment.modelform_mixins import AppointmentFormMixin

from ..models import Appointment


class AppointmentForm(AppointmentFormMixin, forms.ModelForm):

    appt_reason = forms.ChoiceField(
        label='Reason for appointment:',
        choices=APPOINTMENT_REASON,
        widget=forms.RadioSelect)

    class Meta:
        model = Appointment
        fields = '__all__'
