from django.db import models
from edc_constants.choices import YES_NO

from ..choices import CANCER_TREATMENT_GOAL, CHEMO_INTENT
from .model_mixins import CrfModelMixin


class OncologyTreatmentPlan (CrfModelMixin):

    """ ca004 """
    # This is a new question with options from chemo_intent
    treatment_goal = models.CharField(
        verbose_name='What is the goal of cancer treatment?',
        max_length=15,
        choices=CANCER_TREATMENT_GOAL,
    )

    treatment_plan = models.CharField(
        verbose_name='Has a treatment plan been determined?',
        max_length=3,
        choices=YES_NO,
    )

    chemotherapy = models.CharField(
        verbose_name='Is chemotherapy planned?',
        max_length=3,
        null=True,
        blank=True,
        choices=YES_NO,
    )
    # This question remains the same but two options have been removed to new
    # Q: treatment_goal
    # To do:
    # Data migration for responses here to move them to newQ
    chemo_intent = models.CharField(
        verbose_name='What was the intent of giving chemotherapy?',
        max_length=25,
        choices=CHEMO_INTENT,
        null=True,
        blank=True,
    )

    radiation_plan = models.CharField(
        verbose_name='Is radiation therapy planned?',
        max_length=3,
        null=True,
        blank=True,
        choices=YES_NO,
    )

#     radiation_treatments = models.CharField(
#         verbose_name='How many radiation treatments are planned?',
#         max_length=15,
#         null=True,
#         blank=True,
#         help_text='',
#         )

    surgical_plan = models.CharField(
        verbose_name='Is surgical therapy planned?',
        max_length=3,
        null=True,
        blank=True,
        choices=YES_NO,
    )

    planned_operation = models.CharField(
        verbose_name='Describe planned operation',
        max_length=150,
        null=True,
        blank=True,
    )

    comments = models.TextField(
        verbose_name='Comments',
        null=True,
        blank=True,
        max_length=250,
    )

    class Meta(CrfModelMixin.Meta):
        app_label = 'cancer_subject'
        verbose_name = 'Oncology Treatment Plan'
