from datetime import datetime, time
from django.db import models

from edc_base.model_fields import IsDateEstimatedField

from edc.entry_meta_data.managers import EntryMetaDataManager
from edc.subject.adverse_event.models import BaseBaseDeath

from .subject_off_study_mixin import SubjectOffStudyMixin
from cancer_subject.models.old_subject_visit import SubjectVisit


class SubjectDeath (SubjectOffStudyMixin, BaseBaseDeath):

    # added on upgrade
    is_death_date_estimated = IsDateEstimatedField(
        verbose_name="Is date of death estimated?",
        null=True,
        blank=False,
    )

    subject_visit = models.OneToOneField(SubjectVisit)

    entry_meta_data_manager = EntryMetaDataManager(SubjectVisit)

    class Meta:
        app_label = "cancer_subject"
        verbose_name = "Subject Death"
