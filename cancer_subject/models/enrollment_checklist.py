from django.db import models
from edc_base.model_managers.historical_records import HistoricalRecords
from edc_base.model_mixins.base_uuid_model import BaseUuidModel
from edc_base.model_validators.eligibility import eligible_if_yes
from edc_constants.choices import YES_NO
from edc_visit_schedule.model_mixins import EnrollmentModelMixin

from edc_appointment.model_mixins import CreateAppointmentsMixin


ENROLLMENT_SITES = (
    ('gaborone_private_hospital', ' Gaborone Private Hospital (GPH)'),
    ('nyangabgwe_referral_Hospital', 'Nyangabgwe Referral Hospital (NRH)'),
    ('princess_marina_hospital', 'Princess Marina Hospital (PMH)'),
    ('bokamoso_private_hospital', 'Bokamoso Private Hospital (BPH)'),
)


class EnrollmentManager(models.Manager):

    def get_by_natural_key(self, subject_identifier):
        return self.get(
            subject_identifier=subject_identifier
        )


# class CancerEnrollmentModelMixin(models.Model):
#
#     is_eligible = models.BooleanField(default=False)
#
#     loss_reason = models.TextField(
#         verbose_name='Reason not eligible',
#         max_length=500,
#         null=True,
#         editable=False,
#         help_text='(stored for the loss form)')
#
#     objects = EnrollmentManager()
#
#     def natural_key(self):
#         return (self.subject_identifier,)
#
#     class Meta:
#         abstract = True


class EnrollmentChecklist (
        EnrollmentModelMixin, CreateAppointmentsMixin, BaseUuidModel):

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

    def save(self, *args, **kwargs):
        #self.facility_name = 'clinic'
        super().save(*args, **kwargs)

    class Meta(EnrollmentModelMixin.Meta):
        consent_model = 'cancer_subject.subjectconsent'
        visit_schedule_name = 'visit_schedule1.schedule1'
