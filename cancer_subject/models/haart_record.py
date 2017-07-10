from django.db import models

from edc.audit.audit_trail import AuditTrail

from .base_scheduled_visit_model import BaseScheduledVisitModel
from ..choices.haart_record import HAART_STATUS_CHOICE
from .locator import Locator
from cancer_subject.models.model_mixins.crf_model_mixin import CrfModelMixin


class HaartRecord(CrfModelMixin):

    """ MC034"""

#    hiv = models.CharField(
#        verbose_name="1. Does patient have HIV?",
#        max_length=9,
#        choices=YES_NO_DONT_KNOW,
#        help_text="",
#        )

    haart_status = models.CharField(
        verbose_name=("What is the status of the participant's "
                        "antiretroviral treatment (HAART)?"),
        max_length=145,
        null=True,
        blank=True,
        choices=HAART_STATUS_CHOICE,
        help_text="",
        )

    comments = models.TextField(
        verbose_name="Comments",
        max_length=150,
        null=True,
        blank=True,
        help_text="",
        )

    history = AuditTrail()

    def locator(self):
        if Locator.objects.filter(subject_visit__appointment__registered_subject=self.get_visit().appointment.registered_subject).exists():
            l = Locator.objects.get(subject_visit__appointment__registered_subject=self.get_visit().appointment.registered_subject)
            return '<A href="{0}">locator</A>'.format(l.get_absolute_url())
        else:
            return None
    locator.allow_tags = True

    def get_visit(self):
        return self.subject_visit

    def __unicode__(self):
        return unicode(self.subject_visit)

    class Meta:
        app_label = "cancer_subject"
        verbose_name = "Haart Record"
