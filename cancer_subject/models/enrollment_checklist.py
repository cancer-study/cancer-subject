import re
from django.db import models

from edc_base.model_managers.historical_records import HistoricalRecords
from edc_base.model_mixins.base_uuid_model import BaseUuidModel
from edc_base.model_validators.eligibility import eligible_if_yes
from edc_constants.choices import YES_NO
from edc_constants.constants import UUID_PATTERN
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierModelMixin


class SubjectScreeningManager(models.Manager):

    def get_by_natural_key(self, screening_identifier):
        return self.get(screening_identifier=screening_identifier)


class ScreeningIdentifierModelMixin(
        NonUniqueSubjectIdentifierModelMixin, models.Model):

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


class EnrollmentModelMixin(models.Model):

    age_helper_cls = AgeHelper

    is_eligible = models.BooleanField(default=False)

    age_in_years = models.IntegerField(
        null=True,
        editable=False)

    loss_reason = models.TextField(
        verbose_name='Reason not eligible',
        max_length=500,
        null=True,
        editable=False,
        help_text='(stored for the loss form)')

    non_citizen = models.BooleanField(
        default=False,
        help_text='')

    def common_clean(self):

        super().common_clean()

    def save(self, *args, **kwargs):
        pass
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class EnrollmentChecklist (
        EnrollmentModelMixin, ScreeningIdentifierModelMixin, BaseUuidModel):

    has_diagnosis = models.CharField(
        verbose_name="Has a cancer diagnosis been documented? ",
        max_length=3,
        choices=YES_NO,
        validators=[eligible_if_yes, ],
        help_text="( if 'NO' STOP patient cannot be enrolled )",
    )

    enrollment_site = models.CharField(
        max_length=100,
        null=True,
        choices=ENROLLMENT_SITES,
        help_text="Hospital where subject is recruited")

    history = HistoricalRecords()

    class Meta:
        verbose_name = "Enrollment Checklist"
        verbose_name_plural = "Enrollment Checklist"
