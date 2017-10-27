import re
from uuid import uuid4

from django.core.validators import (RegexValidator, MinLengthValidator,
                                    MaxLengthValidator)
from django.db import models
from django_crypto_fields.fields.firstname_field import FirstnameField
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators.date import datetime_not_future
from edc_base.utils import get_utcnow
from edc_constants.choices import (YES_NO, YES_NO_NA, NO, YES,
                                   GENDER_UNDETERMINED, YES_NO_UNKNOWN)
from edc_constants.constants import UUID_PATTERN, NOT_APPLICABLE, OTHER
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierModelMixin
from edc_search.model_mixins import SearchSlugManager

from cancer_subject.constants import ABLE_TO_PARTICIPATE, MENTAL_INCAPACITY

from ..screening_identifier import ScreeningIdentifier


class SubjectScreeningManager(SearchSlugManager, models.Manager):

    def get_by_natural_key(self, screening_identifier):
        return self.get(screening_identifier=screening_identifier)


# from cancer_subject.choices import INABILITY_TO_PARTICIPATE_REASON
# from ..choices import (
#     ENROLLMENT_SITES, INABILITY_TO_PARTICIPATE_REASON)
ENROLLMENT_SITES = (
    ('gaborone_private_hospital', ' Gaborone Private Hospital (GPH)'),
    ('nyangabgwe_referral_Hospital', 'Nyangabgwe Referral Hospital (NRH)'),
    ('princess_marina_hospital', 'Princess Marina Hospital (PMH)'),
    ('bokamoso_private_hospital', 'Bokamoso Private Hospital (BPH)'),
)

INABILITY_TO_PARTICIPATE_REASON = (
    (ABLE_TO_PARTICIPATE, ('ABLE to participate')),
    (MENTAL_INCAPACITY, ('Mental Incapacity')),
    ('Deaf/Mute', ('Deaf/Mute')),
    ('Too sick', ('Too sick')),
    ('Incarcerated', ('Incarcerated')),
    (OTHER, ('Other, specify.')),
    (NOT_APPLICABLE, ('Not applicable')),
)


class EligibilityIdentifierModelMixin(NonUniqueSubjectIdentifierModelMixin, models.Model):

    def update_subject_identifier_on_save(self):
        """Overridden to not set the subject identifier on save.
        """
        if not self.subject_identifier:
            self.subject_identifier = self.subject_identifier_as_pk.hex
        elif re.match(UUID_PATTERN, self.subject_identifier):
            pass
        return self.subject_identifier

    def make_new_identifier(self):
        return self.subject_identifier_as_pk.hex

    class Meta:
        abstract = True


class SubjectEligibility(EligibilityIdentifierModelMixin, BaseUuidModel):

    reference = models.UUIDField(
        verbose_name="Reference",
        unique=True,
        default=uuid4,
        editable=False)

    screening_identifier = models.CharField(
        verbose_name='Eligibility Id',
        max_length=50,
        blank=True,
        unique=True,
        editable=False)

    report_datetime = models.DateTimeField(
        verbose_name='Report date',
        default=get_utcnow,
        validators=[datetime_not_future])

    first_name = FirstnameField(
        verbose_name='First name',
        validators=[RegexValidator("^[A-Z]{1,250}$", "Ensure first name is in CAPS and "
                                   "does not contain any spaces or numbers")],
        null=True,
        help_text="")

    initials = models.CharField(
        verbose_name='Initials',
        max_length=3,
        validators=[
            MinLengthValidator(2),
            MaxLengthValidator(3),
            RegexValidator("^[A-Z]{1,3}$", "Must be Only CAPS and 2 or 3 letters. No spaces or numbers allowed.")],
        null=True,
        help_text="")

    age_in_years = models.IntegerField(
        verbose_name='Age in years as reported by patient',
        null=True,)

    guardian = models.CharField(
        verbose_name="If minor, is there a guardian available? ",
        max_length=10,
        choices=YES_NO_NA,
        null=True,
        help_text="If a minor age 16 and 17, ensure a guardian is available otherwise"
                  " participant will not be enrolled.")

    gender = models.CharField(
        verbose_name='Gender',
        max_length=1,
        null=True,
        choices=GENDER_UNDETERMINED)

    has_identity = models.CharField(
        verbose_name="[Interviewer] Has the subject presented a valid OMANG or other identity document?",
        max_length=10,
        choices=YES_NO,
        null=True,
        help_text='Allow Omang, Passport number, driver\'s license number or Omang receipt number. '
                  'If \'NO\' participant will not be enrolled.')

    citizen = models.CharField(
        verbose_name="Are you a Botswana citizen? ",
        max_length=7,
        choices=YES_NO_UNKNOWN,
        null=True,
        help_text="")

    legal_marriage = models.CharField(
        verbose_name="If not a citizen, are you legally married to a Botswana Citizen?",
        max_length=3,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
        null=True,
        help_text="If 'NO' participant is not eligible.")

    marriage_certificate = models.CharField(
        verbose_name=(
            "[Interviewer] Has the participant produced the marriage certificate, as proof? "),
        max_length=3,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
        null=True,
        help_text="If 'NO' participant is not eligible.")

    literacy = models.CharField(
        verbose_name="Is the participant LITERATE?, or if ILLITERATE, is there a"
                     "  LITERATE witness available ",
        max_length=7,
        choices=YES_NO_UNKNOWN,
        null=True,
        help_text="If participate is illiterate, confirm there is a literate"
                  "witness available otherwise participant is not eligible.")

    inability_to_participate = models.CharField(
        verbose_name="Do any of the following reasons apply to the participant?",
        max_length=17,
        choices=INABILITY_TO_PARTICIPATE_REASON,
        null=True,
        help_text=("Participant can only participate if NONE is selected. "
                   "(Any of these reasons make the participant unable to take "
                   "part in the informed consent process)"),
    )

    cancer_status = models.CharField(
        verbose_name="Has a cancer diagnosis been documented?",
        max_length=30,
        choices=YES_NO,
        help_text='If NO, participant is not eligible.'
    )

    enrollment_site = models.CharField(
        max_length=100,
        null=True,
        choices=ENROLLMENT_SITES,
        help_text="Hospital where subject is recruited")

    eligible = models.BooleanField(
        default=False,
        editable=False)

    reasons_ineligible = models.TextField(
        verbose_name="Reason not eligible",
        max_length=150,
        null=True,
        editable=False)

    objects = SubjectScreeningManager()

    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        if not self.id:
            self.screening_identifier = ScreeningIdentifier().identifier
            self.update_subject_identifier_on_save()
        self.registration_identifier = self.screening_identifier
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.screening_identifier} {self.first_name} ({self.initials}) {self.gender}/{self.age_in_years}'

    def natural_key(self):
        return (self.screening_identifier,)

    class Meta:
        verbose_name = 'Subject Eligibility'
