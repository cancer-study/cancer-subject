from django.apps import apps as django_apps
from django.db import models
from django.db.models.deletion import PROTECT
from edc_base.model_mixins import BaseUuidModel
from edc_consent.model_mixins import RequiresConsentFieldsModelMixin
from edc_lab.models.model_mixins.requisition import RequisitionIdentifierMixin
from edc_lab.models.model_mixins.requisition import RequisitionModelMixin
from edc_lab.models.model_mixins.requisition import RequisitionStatusMixin
from edc_metadata.model_mixins.updates import (
    UpdatesRequisitionMetadataModelMixin)
from edc_offstudy.model_mixins import OffstudyModelMixin
from edc_search.model_mixins import SearchSlugManager
from edc_visit_tracking.managers import (
    CrfModelManager as VisitTrackingCrfModelManager)
from edc_visit_tracking.model_mixins import (
    CrfModelMixin as VisitTrackingCrfModelMixin)
from edc_visit_tracking.model_mixins import PreviousVisitModelMixin

from .model_mixins.search_slug_model_mixin import SearchSlugModelMixin
from .subject_visit import SubjectVisit


class Manager(VisitTrackingCrfModelManager, SearchSlugManager):
    pass


class SubjectRequisition(
    RequisitionModelMixin, RequisitionStatusMixin,
    RequisitionIdentifierMixin,
    VisitTrackingCrfModelMixin,
    OffstudyModelMixin,
    RequiresConsentFieldsModelMixin,
    PreviousVisitModelMixin,
    UpdatesRequisitionMetadataModelMixin,
        SearchSlugModelMixin, BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit, on_delete=PROTECT)
    search_slug_fields = [
        'subject_identifier', 'requisition_identifier',
        'human_readable_identifier', 'identifier_prefix']

    objects = Manager()

    def save(self, *args, **kwargs):
        if not self.id:
            edc_protocol_app_config = django_apps.get_app_config(
                'edc_protocol')
            self.study_site = edc_protocol_app_config.site_code
            self.study_site_name = edc_protocol_app_config.site_name
        super().save(*args, **kwargs)

    def get_search_slug_fields(self):
        fields = super().get_search_slug_fields()
        fields.extend([
            'subject_identifier', 'requisition_identifier',
            'human_readable_identifier', 'identifier_prefix'])
        return fields

    class Meta (VisitTrackingCrfModelMixin.Meta,
                RequiresConsentFieldsModelMixin.Meta):
        app_label = 'cancer_subject'
