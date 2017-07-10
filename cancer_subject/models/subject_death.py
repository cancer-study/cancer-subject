from datetime import datetime, time
from django.core.urlresolvers import reverse
from django.db import models

from edc.audit.audit_trail import AuditTrail
from edc.base.model.fields import IsDateEstimatedField
from edc.entry_meta_data.managers import EntryMetaDataManager
from edc.subject.adverse_event.models import BaseBaseDeath

from .subject_off_study_mixin import SubjectOffStudyMixin
from cancer_subject.models.old_subject_visit import SubjectVisit


class SubjectDeath (SubjectOffStudyMixin, BaseBaseDeath):

    #added on upgrade
    is_death_date_estimated = IsDateEstimatedField(
        verbose_name="Is date of death estimated?",
        null=True,
        blank=False,
        )

    history = AuditTrail()

    subject_visit = models.OneToOneField(SubjectVisit)

    entry_meta_data_manager = EntryMetaDataManager(SubjectVisit)

    def get_report_datetime(self):
        return datetime.combine(self.death_date, time(0, 0))

    def get_absolute_url(self):
        return reverse('admin:cancer_subject_subjectdeath_change', args=(self.id,))

    class Meta:
        app_label = "cancer_subject"
        verbose_name = "Subject Death"
