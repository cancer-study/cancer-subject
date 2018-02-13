from django.db import models

from edc_constants.choices import NOT_APPLICABLE, SEVERITY_LEVEL, YES_NO_UNSURE

from .model_mixins import CrfModelMixin


class CurrentSymptoms (CrfModelMixin):

    any_worry = models.CharField(
        verbose_name=(
            'Does the patient have any symptoms they are worried about?'),
        max_length=15,
        choices=YES_NO_UNSURE,
    )

    symptom_desc = models.TextField(
        verbose_name='If so, describe their symptom:',
        max_length=150,
        null=True,
        blank=True,
    )

    patient_own_remedy = models.TextField(
        verbose_name='What has the patient tried to do about the symptom?',
        max_length=250,
        null=True,
        blank=True,
    )

    severity = models.CharField(
        verbose_name='Severity:',
        max_length=250,
        choices=SEVERITY_LEVEL,
        default=NOT_APPLICABLE,
        blank=False,
        null=True,
        help_text=('If you determine that participant could have '
                   'Grade 4 illness please assist '
                   'them to as best as possible by immediately '
                   'informing the Oncology clinicians '
                   'and the Study Coordinator.'),
    )

    ra_advice = models.TextField(
        verbose_name='What did the RA do to help?',
        max_length=250,
        null=True,
        blank=True,
    )

    outcome_update = models.TextField(
        verbose_name='Outcome or Update:',
        max_length=250,
        null=True,
        blank=True,
    )

    class Meta(CrfModelMixin.Meta):
        app_label = 'cancer_subject'
        verbose_name = 'Current Symptoms'
        verbose_name_plural = 'Current Symptoms'
