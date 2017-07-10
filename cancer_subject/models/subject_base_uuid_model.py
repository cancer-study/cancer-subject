from edc.subject.consent.models.base_consented_uuid_model import BaseConsentedUuidModel
from .subject_off_study_mixin import SubjectOffStudyMixin


class SubjectBaseUuidModel(SubjectOffStudyMixin, BaseConsentedUuidModel):

    """ Base model for all subject models """

    class Meta:
        abstract = True
