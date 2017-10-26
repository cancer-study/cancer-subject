import re
from uuid import uuid4

from django.core.validators import RegexValidator, MinLengthValidator,\
    MaxLengthValidator
from django.db import models
from django_crypto_fields.fields.firstname_field import FirstnameField
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators.date import datetime_not_future
from edc_base.utils import get_utcnow
from edc_constants.choices import YES_NO, YES_NO_NA, NO, YES,\
    GENDER_UNDETERMINED, YES_NO_UNKNOWN
from edc_constants.constants import UUID_PATTERN, NOT_APPLICABLE
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierModelMixin

from cancer_screening.choices import INABILITY_TO_PARTICIPATE_REASON,\
    ENROLLMENT_SITES
from cancer_screening.managers import EligibilityManager

from ..eligibility import Eligibility
from ..eligibility_identifier import EligibilityIdentifier


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
        help_text="")

    initials = models.CharField(
        verbose_name='Initials',
        max_length=3,
        validators=[
            MinLengthValidator(2),
            MaxLengthValidator(3),
            RegexValidator("^[A-Z]{1,3}$", "Must be Only CAPS and 2 or 3 letters. No spaces or numbers allowed.")],
        help_text="")

    age_in_years = models.IntegerField(
        verbose_name='Age in years as reported by patient')

    guardian = models.CharField(
        verbose_name="If minor, is there a guardian available? ",
        max_length=10,
        choices=YES_NO_NA,
        help_text="If a minor age 16 and 17, ensure a guardian is available otherwise"
                  " participant will not be enrolled.")

    gender = models.CharField(
        verbose_name='Gender',
        max_length=1,
        choices=GENDER_UNDETERMINED)

    has_identity = models.CharField(
        verbose_name="[Interviewer] Has the subject presented a valid OMANG or other identity document?",
        max_length=10,
        choices=YES_NO,
        help_text='Allow Omang, Passport number, driver\'s license number or Omang receipt number. '
                  'If \'NO\' participant will not be enrolled.')

    citizen = models.CharField(
        verbose_name="Are you a Botswana citizen? ",
        max_length=7,
        choices=YES_NO_UNKNOWN,
        help_text="")

    legal_marriage = models.CharField(
        verbose_name="If not a citizen, are you legally married to a Botswana Citizen?",
        max_length=3,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
        help_text="If 'NO' participant is not eligible.")

    marriage_certificate = models.CharField(
        verbose_name=(
            "[Interviewer] Has the participant produced the marriage certificate, as proof? "),
        max_length=3,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
        help_text="If 'NO' participant is not eligible.")

    literacy = models.CharField(
        verbose_name="Is the participant LITERATE?, or if ILLITERATE, is there a"
                     "  LITERATE witness available ",
        max_length=7,
        choices=YES_NO_UNKNOWN,
        help_text="If participate is illiterate, confirm there is a literate"
                  "witness available otherwise participant is not eligible.")

    inability_to_participate = models.CharField(
        verbose_name="Do any of the following reasons apply to the participant?",
        max_length=17,
        choices=INABILITY_TO_PARTICIPATE_REASON,
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

    objects = EligibilityManager()

    history = HistoricalRecords()

#     def save(self, *args, **kwargs):
#         self.verify_eligibility()
#         if not self.id:
#             self.screening_identifier = EligibilityIdentifier().identifier
#         super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.verify_eligibility()
        if not self.id:
            self.screening_identifier = EligibilityIdentifier().identifier
            self.update_subject_identifier_on_save()
        eligibility = Eligibility(
            age=self.age_in_years, literate=self.literacy,
            guardian=self.guardian, legal_marriage=self.legal_marriage,
            marriage_certificate=self.marriage_certificate,
            citizen=self.citizen, cancer_status=self.cancer_status,
            participation=self.inability_to_participate)
        self.is_eligible = eligibility.eligible
        self.loss_reason = eligibility.reasons
        self.registration_identifier = self.screening_identifier
        self.update_mapper_fields
        super().save(*args, **kwargs)

#     def __str__(self):
# return f'{self.screening_identifier} {self.gender} {self.age_in_years}'

    def __str__(self):
        return f'{self.screening_identifier} {self.first_name} ({self.initials}) {self.gender}/{self.age_in_years}'

    def natural_key(self):
        return (self.screening_identifier,)

    def verify_eligibility(self):
        """Verifies eligibility criteria and sets model attrs.
        """
        def if_yes(value):
            return True if value == YES else False

        def if_no(value):
            return True if value == NO else False

        eligibility = Eligibility(
            age=self.age_in_years,
            guardian=if_yes(self.guardian),
            cancer_status=if_yes(self.cancer_status))
        self.reasons_ineligible = ','.join(eligibility.reasons)
        self.eligible = eligibility.eligible

    class Meta:
        verbose_name = 'Subject Eligibility'
