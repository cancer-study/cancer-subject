from django.db import models

from .model_mixins import CrfModelMixin

from ..choices import HAART_STATUS_CHOICE


class HaartRecord(CrfModelMixin):

    haart_status = models.CharField(
        verbose_name=('What is the status of the participant\'s '
                      'antiretroviral treatment (HAART)?'),
        max_length=250,
        choices=HAART_STATUS_CHOICE,
        null=True,
        blank=True,
    )

    comments = models.TextField(
        verbose_name='Comments',
        max_length=150,
        null=True,
        blank=True,
    )

    class Meta(CrfModelMixin.Meta):
        app_label = 'cancer_subject'
        verbose_name = 'Haart Record'
