from django.db import models
from edc_base.model_mixins import BaseUuidModel


class DeathReport(BaseUuidModel):
    subject_identifier = models.CharField(
        max_length=50)
