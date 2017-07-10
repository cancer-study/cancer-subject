from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
from edc.subject.off_study.models.base_off_study import BaseOffStudy
from edc.entry_meta_data.managers import EntryMetaDataManager

from cancer_subject.models.old_subject_visit import SubjectVisit


class SubjectOffStudy(BaseOffStudy):

    history = AuditTrail()

    subject_visit = models.OneToOneField(SubjectVisit)

    entry_meta_data_manager = EntryMetaDataManager(SubjectVisit)

    def __unicode__(self):
        return '%s ' % (self.registered_subject)

    def get_visit(self):
        return self.subject_visit

    def get_absolute_url(self):
        return reverse('admin:cancer_subject_subjectoffstudy_change', args=(self.id,))

    class Meta:
        app_label = "cancer_subject"
        verbose_name = "Subject Off Study"
        verbose_name_plural = "Subject Off Study"
