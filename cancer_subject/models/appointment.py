from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel

from edc_appointment.managers import AppointmentManager
from edc_appointment.model_mixins import AppointmentModelMixin


class Appointment(AppointmentModelMixin, BaseUuidModel):

    objects = AppointmentManager()

    history = HistoricalRecords()
