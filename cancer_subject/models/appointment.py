from edc_appointment.managers import AppointmentManager
from edc_appointment.model_mixins import AppointmentModelMixin
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel


class Appointment(AppointmentModelMixin, BaseUuidModel):

    objects = AppointmentManager()

    history = HistoricalRecords()

    def natural_key(self):
        return (self.subject_identifier,
                self.visit_schedule_name,
                self.schedule_name,
                self.visit_code,
                self.visit_code_sequence)

    @property
    def previous(self):
        previous_appt = None
        previous_visit = self.schedule.visits.previous(self.visit_code)
        if previous_visit:
            options = dict(
                subject_identifier=self.subject_identifier,
                visit_schedule_name=self.visit_schedule_name,
                visit_code=previous_visit.code,
                visit_code_sequence=0)
            try:
                previous_appt = self.__class__.objects.get(
                    schedule_name=self.schedule_name,
                    **options)
            except self.__class__.DoesNotExist:
                try:
                    previous_appt = self.__class__.objects.get(**options)
                except self.__class__.DoesNotExist:
                    pass
        return previous_appt

    @property
    def next(self):
        """Returns the next appointment or None in this schedule
        for visit_code_sequence=0.
        """
        next_appt = None
        next_visit = self.schedule.visits.next(self.visit_code)
        if next_visit:
            options = dict(
                subject_identifier=self.subject_identifier,
                visit_schedule_name=self.visit_schedule_name,
                visit_code=next_visit.code,
                visit_code_sequence=0)
            try:
                next_appt = self.__class__.objects.get(
                    schedule_name=self.schedule_name,
                    **options)
            except self.__class__.DoesNotExist:
                try:
                    next_appt = self.__class__.objects.get(**options)
                except self.__class__.DoesNotExist:
                    pass
        return next_appt

    class Meta(AppointmentModelMixin.Meta):
        pass
