from django.db import models
from bhp_common.models import MyBasicUuidModel
# from cancer.choices import OFF_STUDY_CODE_CHOICE

'''
copy the following to your ModelAdmin class in admin.py
class Af004Admin (MyModelAdmin):
    fields = (

        'date_off_study',
        'date_last_contact',
        'off_study_reason',
        'off_study_code',
        'comments',
    )
    radio_fields = {

        "off_study_code":admin.VERTICAL,

    }
admin.site.register(Af004, Af004Admin)
'''
"""
class Af004 (MyBasicUuidModel):


    OFF_STUDY_CODE_CHOICE = (
        ('Completion of protocol required period of time for observation (see MOP for definition of Completion.)','Completion of protocol required period of time for observation (see MOP for definition of Completion.)'),
        ('Death (complete the AF005 Death Record form)','Death (complete the AF005 Death Record form)'),
        ('Participant refused further contact (explain in Comments below)','Participant refused further contact (explain in Comments below)'),
        ('Unable to contact Participant despite repeated attempts (see MOP for definition of Lost to Follow-Up.)','Unable to contact Participant despite repeated attempts (see MOP for definition of Lost to Follow-Up.)'),
        ('Other, specify: ','Other, specify: '),
    )


    date_off_study = models.DateTimeField(
        verbose_name = "1. Date Participant off-study: ",
        max_length =25,
        help_text="dd/mm/yyyy",
        )

    date_last_contact = models.DateTimeField(
        verbose_name = "2. Date of last contact: ",
        max_length =25,
        help_text="dd/mm/yyyy",
        )

    off_study_reason = models.CharField(
        verbose_name = "3. Describe the primary reason for going off-study: ",
        max_length = 35,
        help_text="",
        )

    off_study_code = models.CharField(
        verbose_name = "4. Based on description above, code the primary reason for the Participant to be going off Study:",
        max_length = 105,
        choices = OFF_STUDY_CODE_CHOICE,
        help_text="",
        )

    comments = models.CharField(
        verbose_name = "6. Comments:",
        max_length = 35,
        )

    class Meta:
        app_label = "cancer"
        verbose_name = "AF004 Off Study Record"

"""
