from django.db import models

from edc.audit.audit_trail import AuditTrail
from edc.choices.common import YES_NO

from ..models.base_subject_registered_subject_model import BaseSubjectRegisteredSubjectModel
from ..choices.referral import WHY_REFERRED


class  Referral (BaseSubjectRegisteredSubjectModel):

    """ CA011 """

    report_datetime = models.DateTimeField(null=True)

    referrals = models.CharField(
        verbose_name=("1. Have any referrals been made that should be reported been made "
                      "(by study team or hospital staff)?"),
        max_length=3,
        choices=YES_NO,
        help_text="( if 'No' , STOP and return form to DMC. )",
        )

    why_referred = models.CharField(
        verbose_name="2. Where and why has patient been referred?",
        max_length=75,
        choices=WHY_REFERRED,
        help_text="",
        )

    referral_date = models.DateTimeField(
        verbose_name="3. Date of referral?",
        max_length=25,
        help_text="dd/mm/yyyy",
        )

    comments = models.CharField(
        verbose_name="4. Comments",
        max_length=35,
        help_text="",
        )

    history = AuditTrail()

    def get_report_datetime(self):
        return self.report_datetime

    class Meta:
        app_label = "cancer_subject"
        verbose_name = "Referral"
