from django.apps import apps as django_apps
from django.core.exceptions import ImproperlyConfigured
from django.db import models
from edc_base.model_mixins.constants import DEFAULT_BASE_FIELDS
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierModelMixin
from edc_registration.model_mixins import (
    UpdatesOrCreatesRegistrationModelMixin as BaseUpdatesOrCreatesRegistrationModelMixin)
from edc_search.model_mixins import SearchSlugManager

from edc_consent.field_mixins import ReviewFieldsMixin, PersonalFieldsMixin
from edc_consent.field_mixins import SampleCollectionFieldsMixin, CitizenFieldsMixin
from edc_consent.field_mixins import VulnerabilityFieldsMixin
from edc_consent.field_mixins.bw import IdentityFieldsMixin
from edc_consent.managers import ConsentManager as SubjectConsentManager
from edc_consent.model_mixins import ConsentModelMixin

from ..models.model_mixins import SearchSlugModelMixin


class ConsentManager(SubjectConsentManager, SearchSlugManager):

    def get_by_natural_key(self, subject_identifier, version):
        return self.get(
            subject_identifier=subject_identifier, version=version)


class UpdatesOrCreatesRegistrationModelMixin(BaseUpdatesOrCreatesRegistrationModelMixin):

    @property
    def registration_unique_field(self):
        return 'subject_identifier'

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


class SubjectConsent(
        ConsentModelMixin, UpdatesOrCreatesRegistrationModelMixin,
        NonUniqueSubjectIdentifierModelMixin,
        IdentityFieldsMixin, ReviewFieldsMixin, PersonalFieldsMixin,
        SampleCollectionFieldsMixin, CitizenFieldsMixin,
        VulnerabilityFieldsMixin, SearchSlugModelMixin, BaseUuidModel):
    """ A model completed by the user that captures the ICF.
    """

    is_signed = models.BooleanField(default=False, editable=False)

    consent = ConsentManager()

    history = HistoricalRecords()

    def __str__(self):
        return f'{self.subject_identifier} V{self.version}'

    def natural_key(self):
        return (self.subject_identifier, self.version,)

    class Meta(ConsentModelMixin.Meta):
        app_label = 'cancer_subject'
        get_latest_by = 'consent_datetime'
        unique_together = (('subject_identifier', 'version'),
                           ('first_name', 'dob', 'initials', 'version'))
        ordering = ('-created',)
