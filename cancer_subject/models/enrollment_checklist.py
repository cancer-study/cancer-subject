from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
from edc.base.model.validators import eligible_if_yes, datetime_not_before_study_start, datetime_not_future
from edc.choices.common import YES_NO

#from .base_subject_registered_subject_model import BaseSubjectRegisteredSubjectModel
from .base_subject_registration_model import BaseSubjectRegistrationModel
from ..models import EnrollmentSite


class EnrollmentChecklist (BaseSubjectRegistrationModel):

#     registration_datetime = models.DateTimeField("Today's date",
#         validators=[
#             datetime_not_before_study_start,
#             datetime_not_future, ])

    has_diagnosis = models.CharField(
        verbose_name="Has a cancer diagnosis been documented? ",
        max_length=3,
        choices=YES_NO,
        validators=[eligible_if_yes, ],
        help_text="( if 'NO' STOP patient cannot be enrolled )",
        )

    enrollment_site = models.ForeignKey(EnrollmentSite,
        null=True,
#         blank=True,
        help_text="Hospital where subject is recruited")

    history = AuditTrail()

    def get_registration_datetime(self):
        return self.registration_datetime

    def get_report_datetime(self):
        return self.get_registration_datetime()

    def __unicode__(self):
        return unicode(self.registered_subject)

    def get_absolute_url(self):
        return reverse('admin:cancer_subject_enrollmentchecklist_change', \
                        args=(self.id,))

    class Meta:
        app_label = "cancer_subject"
        verbose_name = "Enrollment Checklist"
        verbose_name_plural = "Enrollment Checklist"
