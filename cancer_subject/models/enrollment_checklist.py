from django.db import models
from edc_base.model_managers.historical_records import HistoricalRecords
from edc_base.model_mixins.base_uuid_model import BaseUuidModel
from edc_base.model_validators.eligibility import eligible_if_yes
from edc_constants.choices import YES_NO
from edc_constants.constants import YES
from edc_search.model_mixins import SearchSlugManager

from edc_appointment.model_mixins import AppointmentModelMixin
# from edc_visit_schedule.model_mixins import EnrollmentModelMixin

from ..models.model_mixins import SearchSlugModelMixin


ENROLLMENT_SITES = (
    ('gaborone_private_hospital', ' Gaborone Private Hospital (GPH)'),
    ('nyangabgwe_referral_Hospital', 'Nyangabgwe Referral Hospital (NRH)'),
    ('princess_marina_hospital', 'Princess Marina Hospital (PMH)'),
    ('bokamoso_private_hospital', 'Bokamoso Private Hospital (BPH)'),
)


class EnrollmentManager(SearchSlugManager, models.Manager):

    def get_by_natural_key(self, subject_identifier):
        return self.get(
            subject_identifier=subject_identifier
        )


class EnrollmentChecklist (SearchSlugModelMixin, AppointmentModelMixin,
                           BaseUuidModel):

    objects = EnrollmentManager()

    def natural_key(self):
        return (self.subject_identifier,)

    subject_identifier = models.CharField(
        verbose_name='Subject Identifier',
        max_length=50,
        blank=True,
        unique=True)

    has_diagnosis = models.CharField(
        verbose_name="Has a cancer diagnosis been documented? ",
        max_length=3,
        choices=YES_NO,
        validators=[eligible_if_yes, ],
        help_text="( if 'NO' STOP patient cannot be enrolled )",)

    enrollment_site = models.CharField(
        max_length=100,
        null=True,
        choices=ENROLLMENT_SITES,
        help_text="Hospital where subject is recruited")

    history = HistoricalRecords()

    def create_appointments(self, base_appt_datetime=None, taken_datetimes=None):
        if self.has_diagnosis == YES:
            super().create_appointments(
                base_appt_datetime=base_appt_datetime, taken_datetimes=taken_datetimes)
            self.is_eligible = True
        else:
            self.is_eligible = False

    class Meta():
        consent_model = 'cancer_subject.subjectconsent'
        visit_schedule_name = 'visit_schedule1.schedule1'
