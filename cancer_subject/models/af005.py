# coding: utf-8
from django.db import models
from edc.audit.audit_trail import AuditTrail
if 'edc.device.dispatch' in settings.INSTALLED_APPS:
    from edc.device.dispatch.models import BaseDispatchSyncUuidModel as BaseSyncUuidModel
else:
    from edc.device.sync.models import BaseSyncUuidModel

'''
copy the following to your ModelAdmin class in admin.py
class Af005Admin (MyModelAdmin):
    fields = (

        'death_date',
        'primary_death_cause',
        'death_cause_description',
        'death_cause_category',
        'diagnosis_code',
        'comments',
    )
    radio_fields = {
        "primary_death_cause":admin.VERTICAL,
        "death_cause_category":admin.VERTICAL,

    }
admin.site.register(Af005, Af005Admin)
'''


class Af005 (BaseSyncUuidModel):

    PRIMARY_DEATH_CAUSE_CHOICE = (
        ('No information will ever be available (go to question 6)', 'No information will ever '
         'be available (go to question 6)'),
        ('Autopsy', 'Autopsy'),
        ('Clinical record', 'Clinical record'),
        ('Information from physician/nurse/other health care provider','Information from '
         'physician/nurse/other health care provider'),
        ('Information from participant’s relatives or friends','Information from participant’s '
         'relatives or friends'),
        ('Information requested, still pending','Information requested, still pending'),
        ('Other, specify: ','Other, specify: '),
    )
    DEATH_CAUSE_CATEGORY_CHOICE = (
        ('No information available (go to question 6)', 'No information available (go to question 6)'),
        ('Cancer ', 'Cancer'),
        ('HIV infection or HIV/AIDS-related diagnosis', 'HIV infection or HIV/AIDS-related diagnosis'),
        ('Disease/injury unrelated to cancer or HIV','Disease/injury unrelated to cancer or HIV'),
        ('Toxicity from cancer treatment (complications of chemotherapy, radiation, or surgery)',
         'Toxicity from cancer treatment (complications of chemotherapy, radiation, or surgery)'),
        ('Toxicity from HIV/AIDS treatment (HAART or treatment of HIV/AIDS-related diagnosis)',
         'Toxicity from HIV/AIDS treatment (HAART or treatment of HIV/AIDS-related diagnosis)'),
        ('Other, specify: ','Other, specify: '),
    )

    death_date = models.DateTimeField(
        verbose_name="1. Date of Death: ",
        max_length=25,
        help_text="dd/mm/yyyy",
        )

    primary_death_cause = models.CharField(
        verbose_name="2. What is the primary source of cause of death information? ",
        max_length=65,
        choices=PRIMARY_DEATH_CAUSE_CHOICE,
        help_text="",
        )

    death_cause_description = models.CharField(
        verbose_name="3. Describe the primary cause of death.:  ",
        max_length=35,
        help_text="",
        )

    death_cause_category = models.CharField(
        verbose_name="4. Based on the above description, what category best defines the primary cause of death? ",
        max_length=85,
        choices=DEATH_CAUSE_CATEGORY_CHOICE,
        help_text="",
        )

    diagnosis_code = models.CharField(
        verbose_name="5. Diagnosis code for primary cause of death: ",
        max_length=8,
        help_text="",
        )

    comments = models.CharField(
        verbose_name="6. Comments:",
        max_length=35,
        )

    history = AuditTrail()

    class Meta:
        app_label = "cancer"
        verbose_name = "AF005 Death Record"
