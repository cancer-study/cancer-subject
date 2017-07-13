from django.db import models

from edc_constants.choices import YES_NO
from edc_consent.validators import eligible_if_yes


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

    enrollment_site = models.ForeignKey(
        EnrollmentSite,
        null=True,
        #       blank=True,
        help_text="Hospital where subject is recruited")

    class Meta:
        app_label = "cancer_subject"
        verbose_name = "Enrollment Checklist"
        verbose_name_plural = "Enrollment Checklist"
