from django.db import models

from edc_base.model_mixins import BaseUuidModel
from edc_base.model_managers import HistoricalRecords
from edc_offstudy.model_mixins import OffstudyModelMixin, OffstudyModelManager


class SubjectOffstudy(OffstudyModelMixin, BaseUuidModel):

    """A model completed by the user that completed when the
    subject is taken off-study.
    """

    comment = models.TextField(
        verbose_name="Comment",
        max_length=250,
        blank=True,
        null=True
    )

    objects = OffstudyModelManager()

    history = HistoricalRecords()

    class Meta(OffstudyModelMixin.Meta):
        app_label = "cancer_subject"
        verbose_name_plural = "Subject Off Study"
