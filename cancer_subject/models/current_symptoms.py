from django.db import models

from edc_constants.choices import YES_NO_UNSURE, SEVERITY_LEVEL

from .model_mixins import CrfModelMixin


class CurrentSymptoms (CrfModelMixin):

    """ NEW form on system upgrade"""

    any_worry = models.CharField(
        verbose_name=(
            "Does the patient have any symptoms they are worried "
            "about?"),
        max_length=15,
        choices=YES_NO_UNSURE,
        help_text="",
    )

    symptom_desc = models.TextField(
        verbose_name=("If so, describe their symptom"),
        max_length=150,
        null=True,
        blank=True,
        help_text="",
    )

    patient_own_remedy = models.TextField(
        verbose_name=("What has the patient tried to do about the "
                      "symptom?"),
        max_length=250,
        null=True,
        blank=True,
        help_text="",
    )

    severity = models.CharField(
        verbose_name=("Severity"),
        blank=False,
        null=True,
        default='NOT_APPLICABLE',
        choices=SEVERITY_LEVEL,
        max_length=250,
        help_text=("If you determine that participant could have "
                   "Grade 4 illness please assist "
                   "them to as best as possible by immediately "
                   "informing the Oncology clinicians "
                   "and the Study Coordinator."),
    )

#     pain = models.CharField(
#         verbose_name="Pain",
#         choices=(
#                  ('no pain', 'I have no pain or discomfort'),
#                  ('slight pain', 'I have slight pain or discomfort'),
#                  ('moderate pain', 'I have moderate pain or discomfort'),
#                  ('severe pain', 'I have severe pain or discomfort'),
#                  ('extreme pain', 'I have extreme pain or discomfort'),
#                  ('DWTA', 'Don\'t want to answer'),
#                  ),
#         max_length=45
#         )

    ra_advice = models.TextField(
        verbose_name="What did the RA do to help?",
        null=True,
        blank=True,
        max_length=250)

    outcome_update = models.TextField(
        verbose_name="Outcome or Update",
        null=True,
        blank=True,
        max_length=250)

    class Meta(CrfModelMixin.Meta):
        app_label = "cancer_subject"
        verbose_name = "Current Symptoms"
        verbose_name_plural = "Current Symptoms"
