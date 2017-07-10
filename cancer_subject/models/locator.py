from django.db import models
from django.core.validators import RegexValidator

from edc.audit.audit_trail import AuditTrail
from edc.subject.locator.models import BaseLocator
from edc.choices.common import YES_NO
from edc.base.model.validators import BWCellNumber, BWTelephoneNumber
from edc.core.crypto_fields.fields import EncryptedCharField
from edc.entry_meta_data.managers import EntryMetaDataManager

from ..models import SubjectVisit
from .subject_off_study_mixin import SubjectOffStudyMixin


class Locator(SubjectOffStudyMixin, BaseLocator):

    subject_visit = models.OneToOneField(SubjectVisit)
    #v2 added more fields to key additional contact info for
    #participants who provide more than one contact person
    alt_contact_cell_number = EncryptedCharField(
        max_length=8,
        verbose_name="Cell number (alternate)",
        validators=[BWCellNumber, ],
        help_text="",
        blank=True,
        null=True,
        )
    has_alt_contact = models.CharField(
        max_length=25,
        choices=YES_NO,
        verbose_name=("If we are unable to contact the person indicated above, is there another"
                      " individual (including next of kin) with whom the study team can get"
                      " in contact with?"),
        help_text="",
        )

    alt_contact_name = EncryptedCharField(
        max_length=35,
        verbose_name="Full Name of the responsible person",
        help_text="include firstname and surname",
        blank=True,
        null=True,
        )

    alt_contact_rel = EncryptedCharField(
        max_length=35,
        verbose_name="Relationship to participant",
        blank=True,
        null=True,
        help_text="",
        )
    alt_contact_cell = EncryptedCharField(
        max_length=8,
        verbose_name="Cell number",
        validators=[BWCellNumber, ],
        help_text="",
        blank=True,
        null=True,
        )

    other_alt_contact_cell = EncryptedCharField(
        max_length=8,
        verbose_name="Cell number (alternate)",
        validators=[BWCellNumber, ],
        help_text="",
        blank=True,
        null=True,
        )

    alt_contact_tel = EncryptedCharField(
        max_length=8,
        verbose_name="Telephone number",
        validators=[BWTelephoneNumber, ],
        help_text="",
        blank=True,
        null=True,
        )

    #new fields on upgrade
    local_clinic = models.CharField(
        verbose_name=("When you stay in the village, what clinic/health post do you normally go to?"),
        max_length=75,
        validators=[RegexValidator(
            regex=r'^[0-9]{2}[-][0-9]{1}[-][0-9]{2}$',
            message='The correct clinic code format is XX-X-XX'), ],
        help_text="",
        )
    home_village = models.CharField(
        verbose_name=("Where is your home village?"),
        max_length=75,
        help_text="",
        )

    history = AuditTrail(show_in_admin=True)

    entry_meta_data_manager = EntryMetaDataManager(SubjectVisit)

    def save(self, *args, **kwargs):
        # as long as locator is on a visit schedule, need to update self.registered_subject manually
        if self.subject_visit:
            if not self.registered_subject:
                self.registered_subject = self.registered_subject = self.subject_visit.appointment.registered_subject
        super(Locator, self).save(*args, **kwargs)

    def get_visit(self):
        return self.subject_visit

    def get_subject_identifier(self):
        return self.get_visit().get_subject_identifier()

    def get_report_datetime(self):
        return self.created

    def __unicode__(self):
        return unicode(self.subject_visit)

    class Meta:
        verbose_name = 'Locator'
        app_label = 'cancer_subject'
