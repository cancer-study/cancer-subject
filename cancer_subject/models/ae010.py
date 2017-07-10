from django.db import models

from edc.audit.audit_trail import AuditTrail
from edc. import MyBasicUuidModel

from ..choices import REPORT_TYPE_CHOICE, RELATIONSHIP_DESCRIPTION_CHOICE

'''
copy the following to your ModelAdmin class in admin.py
class Ae010Admin (MyModelAdmin):
    fields = (

        'report_type',
        'onset_date',
        'event_grade',
        'relationship_description',
    )
    radio_fields = {

        "report_type":admin.VERTICAL,
        "relationship_description":admin.VERTICAL,
    }
admin.site.register(Ae010, Ae010Admin)
'''


class Ae010 (MyBasicUuidModel):
    REPORT_TYPE_CHOICE = (
        ('Original report of an event', 'Original report of an event'),
        ('Updated information', 'Updated information'),
        ('Resolution', 'Resolution'),
    )
    RELATIONSHIP_DESCRIPTION_CHOICE = (
        (' Definitely related to study activities', 'Definitely related to study activities'),
        (' Probably related to study activities', 'Probably related to study activities'),
        (' Possibly related to study activities', ' Possibly related to study activities'),
        (' Probably NOT related to study activities', ' Probably NOT related to study activities'),
        (' Not related to study activities', ' Not related to study activities'),
        (' Pending, cannot tell yet if related to study activities', ' Pending, cannot tell yet '
         'if related to study activities'),
    )

    report_type = models.CharField(
        verbose_name="1. Which type of report is this? ",
        max_length=35,
        choices=REPORT_TYPE_CHOICE,
        help_text="",
        )

    onset_date = models.DateTimeField(
        verbose_name="2. Date of onset of event being reported here:",
        max_length=25,
        help_text="",
        )

    event_grade = models.CharField(
        verbose_name="4. =Grade of primary event (use grading scale 1-5, where 5=death) ",
        max_length=15,
        help_text="",
        )

    relationship_description = models.CharField(
        verbose_name=("5. Please describe the relationship between this adverse event and study "
                      "activities:"),
        max_length=65,
        choices=RELATIONSHIP_DESCRIPTION_CHOICE,
        help_text="",
        )

    history = AuditTrail()

    class Meta:
        app_label = "cancer"
        verbose_name = "AE010 Adverse Event Report"
