from django.db import models
from django.core.validators import RegexValidator
from django_crypto_fields.fields.encrypted_char_field import EncryptedCharField

from .subject_visit import SubjectVisit

from edc_base.model_mixins.base_uuid_model import BaseUuidModel
from edc_base.model_validators.bw.validators import (
    BWCellNumber, BWTelephoneNumber)
from edc_consent.model_mixins import RequiresConsentMixin
from edc_locator.model_mixins import LocatorModelMixin

from edc_constants.choices import YES_NO


class SubjectLocator(LocatorModelMixin, RequiresConsentMixin, BaseUuidModel):

    subject_visit = models.OneToOneField(SubjectVisit)
    # v2 added more fields to key additional contact info for
    # participants who provide more than one contact person
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

    # new fields on upgrade
    local_clinic = models.CharField(
        verbose_name=(
            "When you stay in the village, what clinic/health post do you normally go to?"),
        max_length=75,
        validators=[RegexValidator(
            regex=r'^[0-9]{2}[-][0-9]{1}[-][0-9]{2}$',
            message='The correct clinic code format is XX-X-XX'), ],
        help_text="",
    )
    home_village = models.CharField(
        verbose_name=("Where is your home village?"),
        max_length=75,
        help_text="",)

    class Meta:
        verbose_name = 'Locator'
        app_label = 'cancer_subject'
