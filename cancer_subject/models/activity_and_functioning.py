# coding: utf-8
from django.db import models

from edc.audit.audit_trail import AuditTrail

from .base_scheduled_visit_model import BaseScheduledVisitModel
from ..choices.activity_and_functioning import (HEALTH_RATE_CHOICE, HEALTH_PROBLEMS_CHOICE,
                                                             DIFFICULTY_WORK_CHOICE, BODILY_PAIN_CHOICE,
                                                             ENERGY_CHOICE, HEALTH_PROBS_LIMIT_CHOICE,
                                                             EMOTIONAL_PROBS_CHOICE, PROBS_FROM_WORK_CHOICE,
                                                             PERFORM_STATUS_CHOICE)


class ActivityAndFunctioning (BaseScheduledVisitModel):

    """CA003"""

    health_rate = models.CharField(
        verbose_name=("1. Overall, how would you rate your health during "
                        "the PAST 4 WEEKS?"),
        max_length=15,
        choices=HEALTH_RATE_CHOICE,
        help_text="",
        )

    health_problems = models.CharField(
        verbose_name=("2. During the PAST 4 WEEKS, how much did physical "
                       "health problems limit your usual physical activities "
                       "(walking, climbing stairs)?"),
        max_length=35,
        choices=HEALTH_PROBLEMS_CHOICE,
        help_text="",
        )

    difficulty_work = models.CharField(
        verbose_name=("3. During the PAST 4 WEEKS, how much difficulty did "
                        "you have doing your daily work, both at home and "
                        "away from home, because of your physical health?"),
        max_length=35,
        choices=DIFFICULTY_WORK_CHOICE,
        help_text="",
        )

    bodily_pain = models.CharField(
        verbose_name=("4. How much bodily pain have you had during the PAST "
                        "4 WEEKS?"),
        max_length=15,
        choices=BODILY_PAIN_CHOICE,
        help_text="",
        )

    probs_from_work = models.CharField(
    	verbose_name=("8. During the past 4 weeks, how much did personal or emotional problems keep you from doing "
                      "work, school or other daily activities?"),
    	max_length=35,
    	choices=PROBS_FROM_WORK_CHOICE,
    	help_text="",
        )

    energy = models.CharField(
        verbose_name=("5. During the PAST 4 WEEKS, how much energy did you "
                        "have?"),
        max_length=15,
        choices=ENERGY_CHOICE,
        help_text="",
        )

    health_probs_limit = models.CharField(
        verbose_name=("6. During the PAST 4 WEEKS, how much did your "
                        "physical health or emotional problems limit your "
                        "usual social activities with family or friends?"),
        max_length=35,
        choices=HEALTH_PROBS_LIMIT_CHOICE,
        help_text="",
        )

    emotional_probs = models.CharField(
        verbose_name=("7. During the PAST 4 WEEKS, how much have you been "
                        "bothered by emotional problems (such as feeling "
                        "anxious, depressed or irritable)?"),
        max_length=15,
        choices=EMOTIONAL_PROBS_CHOICE,
        help_text="",
        )

    perform_status = models.CharField(
        verbose_name=("9. What is the participant perfomance status, determined by study staff with questioning and "
                      "observation of the participant"),
        max_length=205,
        choices=PERFORM_STATUS_CHOICE,
        help_text="",
        )

    history = AuditTrail()

    def get_visit(self):
        return self.subject_visit

    def __unicode__(self):
        return unicode(self.subject_visit)

    class Meta:
        app_label = "cancer_subject"
        verbose_name = "Activity and Functioning"
        verbose_name_plural = "Activity and Functioning"
