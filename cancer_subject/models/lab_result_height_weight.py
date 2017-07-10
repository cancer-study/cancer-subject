from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from edc.audit.audit_trail import AuditTrail
from edc.choices.common import YES_NO

from .base_scheduled_visit_model import BaseScheduledVisitModel
from cancer_subject.models.model_mixins.crf_model_mixin import CrfModelMixin


class LabResultHeightWeight(CrfModelMixin):

    """CA005 Lab Result : Height Weight Cough patient information to "
       be filled by Recruiter"""

    weight = models.DecimalField(
        verbose_name="Weight",
        max_digits=4,
        decimal_places=1,
        null=True,
        blank=True,
        validators=[MinValueValidator(15), MaxValueValidator(400)],
        help_text="kg"
        )

    height = models.DecimalField(
        verbose_name="Height:",
        max_digits=4,
        decimal_places=1,
        null=True,
        blank=True,
        validators=[MinValueValidator(50), MaxValueValidator(250)],
        help_text="cm"
        )

    cough2weeks = models.CharField(
        verbose_name=("Does the participant have cough (>2 weeks) OR "
                        "weight loss OR drenching night sweats (need to "
                        "change bed clothes/sheets)?"),
        max_length=3,
        choices=YES_NO,
        help_text="",
        )

    history = AuditTrail()

    def get_visit(self):
        return self.subject_visit

    def __unicode__(self):
        return unicode(self.subject_visit)

    class Meta:
        app_label = "cancer_subject"
        verbose_name = "Lab Result: Height & Weight"
        verbose_name_plural = "Lab Result: Height & Weight"
