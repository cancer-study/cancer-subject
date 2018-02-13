from django.db import models

from edc_identifier.model_mixins import NonUniqueSubjectIdentifierModelMixin


class ScreeningIdentifierModelMixin(NonUniqueSubjectIdentifierModelMixin,
                                    models.Model):

    def update_subject_identifier_on_save(self):
        """Overridden to not set the subject identifier on save.
        """
        if not self.subject_identifier:
            self.subject_identifier = self.subject_identifier_as_pk.hex
        return self.subject_identifier

    def make_new_identifier(self):
        return self.subject_identifier_as_pk.hex

    @property
    def registration_unique_field(self):
        return 'registration_identifier'

    @property
    def registered_subject(self):
        """Returns a registered subject instance or None.

        Note: For existing household members Registered Subject must exist
        as it is created when the first household_member instance is created.
        """
        try:
            obj = self.registered_subject_model_class.objects.get(
                registration_identifier=self.registration_identifier)
        except self.registered_subject_model_class.DoesNotExist as e:
            if self.id:
                raise self.registered_subject_model_class.DoesNotExist(
                    'RegisteredSubject instance unexpectedly missing for '
                    'registration_identifier={}. Got {}'.format(
                        self.registration_identifier, str(e)))
            else:
                obj = None
        return obj

    class Meta:
        abstract = True
