from django.db import models
from django.db.models.deletion import PROTECT
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel, FormAsJSONModelMixin
from edc_base.sites.site_model_mixin import SiteModelMixin
from edc_consent.model_mixins import RequiresConsentFieldsModelMixin
from edc_metadata.model_mixins.updates import UpdatesCrfMetadataModelMixin
from edc_reference.model_mixins import ReferenceModelMixin
from edc_visit_schedule.model_mixins import SubjectScheduleCrfModelMixin
from edc_visit_tracking.managers import (
    CrfModelManager as VisitTrackingCrfModelManager)
from edc_visit_tracking.model_mixins import (
    CrfModelMixin as VisitTrackingCrfModelMixin, PreviousVisitModelMixin)
from edc_visit_tracking.model_mixins import CrfModelMixin as BaseCrfModelMixin


from ..subject_visit import SubjectVisit


# from edc_protocol.validators import datetime_not_before_study_start
class CrfModelManager(VisitTrackingCrfModelManager):

    def get_by_natural_key(self, subject_identifier, visit_schedule_name,
                           schedule_name, visit_code):
        return self.get(
            subject_visit__subject_identifier=subject_identifier,
            subject_visit__visit_schedule_name=visit_schedule_name,
            subject_visit__schedule_name=schedule_name,
            subject_visit__visit_code=visit_code
        )


class CrfModelMixin(BaseCrfModelMixin, SubjectScheduleCrfModelMixin,
                    RequiresConsentFieldsModelMixin, PreviousVisitModelMixin,
                    UpdatesCrfMetadataModelMixin, SiteModelMixin,
                    FormAsJSONModelMixin, ReferenceModelMixin, BaseUuidModel):

    """ Base model for all scheduled models
    """

    offschedule_compare_dates_as_datetimes = True
    subject_visit = models.OneToOneField(SubjectVisit, on_delete=PROTECT)

    def natural_key(self):
        return self.subject_visit.natural_key()
    natural_key.dependencies = ['cancer_subject.subjectvisit', 'sites.Site']

    class Meta:
        abstract = True


class CrfModelMixinNonUniqueVisit(BaseCrfModelMixin,
                                  SubjectScheduleCrfModelMixin,
                                  RequiresConsentFieldsModelMixin,
                                  PreviousVisitModelMixin,
                                  SiteModelMixin, UpdatesCrfMetadataModelMixin,
                                  BaseUuidModel):

    """ Base model for all scheduled models
     (adds key to :class:`SubjectVisit`).
    """

    subject_visit = models.OneToOneField(SubjectVisit, on_delete=PROTECT)

    def natural_key(self):
        return self.subject_visit.natural_key()
    natural_key.dependencies = ['cancer_subject.subjectvisit', 'sites.Site']

    class Meta  (VisitTrackingCrfModelMixin.Meta,
                 RequiresConsentFieldsModelMixin.Meta):
        consent_model = 'cancer_subject.subjectconsent'
        abstract = True
