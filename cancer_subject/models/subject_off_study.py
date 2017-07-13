from django.db import models

from edc.subject.off_study.models.base_off_study import BaseOffStudy
from edc.entry_meta_data.managers import EntryMetaDataManager

from cancer_subject.models.old_subject_visit import SubjectVisit


class SubjectOffStudy(BaseOffStudy):

    subject_visit = models.OneToOneField(SubjectVisit)

    entry_meta_data_manager = EntryMetaDataManager(SubjectVisit)

    class Meta:
        app_label = "cancer_subject"
        verbose_name = "Subject Off Study"
        verbose_name_plural = "Subject Off Study"
