import re

from django.core.exceptions import ImproperlyConfigured
from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators.eligibility import eligible_if_yes
from edc_consent.field_mixins import (
    SampleCollectionFieldsMixin, CitizenFieldsMixin)
from edc_consent.field_mixins import ReviewFieldsMixin, PersonalFieldsMixin
from edc_consent.field_mixins import VulnerabilityFieldsMixin
from edc_consent.field_mixins.bw import IdentityFieldsMixin
from edc_consent.model_mixins import ConsentModelMixin
from edc_constants.choices import YES_NO
from edc_constants.constants import UUID_PATTERN
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierModelMixin
from edc_registration.model_mixins import (
    UpdatesOrCreatesRegistrationModelMixin as BaseUpdatesOrCreatesRegistrationModelMixin)

from edc_base.model_mixins.constants import DEFAULT_BASE_FIELDS

from .age_helper import AgeHelper
from .choices import ENROLLMENT_SITES


class UpdatesOrCreatesRegistrationModelMixin(BaseUpdatesOrCreatesRegistrationModelMixin):

    @property
    def registration_unique_field(self):
        return 'registration_identifier'

    @property
    def registration_options(self):
        """Gathers values for common attributes between the
        registration model and this instance.
        """
        registration_options = {}
        for field in self.registration_model._meta.get_fields():
            if (field.name not in DEFAULT_BASE_FIELDS + ['_state'] +
                    [self.registration_unique_field]):
                try:
                    registration_options.update({field.name: getattr(
                        self, field.name)})
                except AttributeError:
                    pass
        return registration_options

    def registration_raise_on_not_unique(self):
        """Asserts the field specified for update_or_create is unique.
        """
        unique_fields = ['registration_identifier']
        for f in self.registration_model._meta.get_fields():
            try:
                if f.unique:
                    unique_fields.append(f.name)
            except AttributeError:
                pass
        if self.registration_unique_field not in unique_fields:
            raise ImproperlyConfigured('Field is not unique. Got {}.{} -- {}'.format(
                self._meta.label_lower, self.registration_unique_field))

    class Meta:
        abstract = True


class SubjectConsent(ConsentModelMixin, UpdatesOrCreatesRegistrationModelMixin,
                     NonUniqueSubjectIdentifierModelMixin, IdentityFieldsMixin,
                     ReviewFieldsMixin, PersonalFieldsMixin,
                     SampleCollectionFieldsMixin, CitizenFieldsMixin,
                     VulnerabilityFieldsMixin  # SearchSlugModelMixin, CreateEnrollment
                     , BaseUuidModel):
    """ A model completed by the user that captures the ICF.
    """

    screening_identifier = models.CharField(
        verbose_name='Eligibility Identifier',
        max_length=50,
        blank=True,
        unique=True)

    registration_identifier = models.CharField(
        verbose_name='Registration Identifier',
        max_length=50,
        blank=True,
        unique=True,
        editable=False)

    is_minor = models.CharField(
        verbose_name=("Is subject a minor?"),
        max_length=10,
        choices=YES_NO,
        null=True,
        blank=False,
        help_text=('Subject is a minor if aged 16-17. A guardian must '
                   'be present for consent. HIV status may NOT be '
                   'revealed in the household.'),
        editable=False)

    is_signed = models.BooleanField(
        default=False,
        editable=False)

    lab_identifier = models.CharField(
        verbose_name=("lab allocated identifier"),
        max_length=50,
        null=True,
        blank=True,
        help_text="if known."
    )

    htc_identifier = models.CharField(
        verbose_name=("HTC Identifier"),
        max_length=50,
        null=True,
        blank=True,
        help_text="if known."
    )

    pims_identifier = models.CharField(
        verbose_name=("PIMS identifier"),
        max_length=50,
        null=True,
        blank=True,
        help_text="if known."
    )

#     objects = SubjectConsentManager()
    history = HistoricalRecords()

    def natural_key(self):
        return (self.subject_identifier, self.registration_identifier,)

    def __str__(self):
        return '{0} V{1}'.format(
            self.subject_identifier,
            self.version)

    def save(self, *args, **kwargs):
        self.registration_identifier = self.screening_identifier
        super().save(*args, **kwargs)

    class Meta(ConsentModelMixin.Meta):
        app_label = "cancer_screening"
        verbose_name = 'Cancer Subject Consent'
        verbose_name_plural = 'Cancer Consent'
        ordering = ('-created',)
