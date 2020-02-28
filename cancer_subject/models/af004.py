from django.db import models

from ..choices import OFF_STUDY_CODE_CHOICE
from .model_mixins import CrfModelMixin


class Af004 (CrfModelMixin):

    date_off_study = models.DateTimeField(
        verbose_name='Date Participant off-study:',
        max_length=25,
        help_text='dd/mm/yyyy',
    )

    date_last_contact = models.DateTimeField(
        verbose_name='Date of last contact:',
        max_length=25,
        help_text='dd/mm/yyyy',
    )

    off_study_reason = models.CharField(
        verbose_name='Describe the primary reason for going off-study:',
        max_length=35,
    )

    off_study_code = models.CharField(
        verbose_name=('Based on description above, code the primary '
                      'reason for the Participant to be going off Study:'),
        max_length=105,
        choices=OFF_STUDY_CODE_CHOICE,
    )

    comments = models.CharField(
        verbose_name='Comments:',
        max_length=150,
    )

    class Meta(CrfModelMixin.Meta):
        app_label = 'cancer_subject'
        verbose_name = 'AF004 Off Study Record'
