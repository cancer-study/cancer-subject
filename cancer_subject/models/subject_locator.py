from django.db import models
from django_crypto_fields.fields import EncryptedCharField
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import CellNumber, TelephoneNumber
from edc_consent.model_mixins import RequiresConsentFieldsModelMixin
from edc_constants.choices import YES_NO_NA, YES_NO, YES, NOT_APPLICABLE
from edc_locator.model_mixins import LocatorModelMixin


class SubjectLocator(LocatorModelMixin, RequiresConsentFieldsModelMixin,
                     BaseUuidModel):
    """A model completed by the user to that captures participant
    locator information and permission to contact.
    """

    home_visit_permission = models.CharField(
        max_length=25,
        choices=YES_NO,
        verbose_name=('Has the participant given his/her permission for study'
                      'staff to make home visits for follow-up purposes?'),
    )

    alt_contact_cell_number = EncryptedCharField(
        max_length=8,
        verbose_name='Cell number (alternate)',
        validators=[CellNumber, ],
        blank=True,
        null=True)

    has_alt_contact = models.CharField(
        max_length=25,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
        verbose_name=(
            'If we are unable to contact the person indicated above, '
            'is there another individual (including next of kin) with '
            'whom the study team can get in contact with?'))

    alt_contact_name = EncryptedCharField(
        max_length=35,
        verbose_name='Full Name of the responsible person',
        help_text='include first name and surname',
        blank=True,
        null=True)

    alt_contact_rel = EncryptedCharField(
        max_length=35,
        verbose_name='Relationship to participant',
        blank=True,
        null=True,
    )
    alt_contact_cell = EncryptedCharField(
        max_length=8,
        verbose_name='Cell number',
        validators=[CellNumber, ],
        blank=True,
        null=True,
    )

    other_alt_contact_cell = EncryptedCharField(
        max_length=8,
        verbose_name='Cell number (alternate)',
        validators=[CellNumber, ],
        help_text='',
        blank=True,
        null=True,
    )

    alt_contact_tel = EncryptedCharField(
        max_length=8,
        verbose_name='Telephone number',
        validators=[TelephoneNumber, ],
        blank=True,
        null=True,
    )

    history = HistoricalRecords()

    def __str__(self):
        return '{}'.format(self.subject_identifier)

    @property
    def formatted_locator_information(self):
        """Returns a formatted string that summarizes contact
        and locator info."""
        info = 'May not follow-up.'
        may_sms_follow_up = ('SMS permitted'
                             if self.may_sms_follow_up == YES else 'NO SMS!')
        if self.may_follow_up == YES:
            info = (
                '{may_sms_follow_up}\n'
                'Cell: {subject_cell} {alt_subject_cell}\n'
                'Phone: {subject_phone} {alt_subject_phone}\n'
                '').format(
                    may_sms_follow_up=may_sms_follow_up,
                    subject_cell='{} (primary)'.format(
                        self.subject_cell) if self.subject_cell else '(none)',
                    alt_subject_cell=self.subject_cell_alt,
                    subject_phone=self.subject_phone or '(none)',
                    alt_subject_phone=self.subject_phone_alt
            )
            if self.may_call_work == YES:
                info = (
                    '{info}\n Work Contacts:\n'
                    '{subject_work_place}\n'
                    'Work Phone: {subject_work_phone}\n'
                    '').format(
                        info=info,
                        subject_work_place=(self.subject_work_place
                                            or '(work place not known)'),
                        subject_work_phone=self.subject_work_phone)
            if self.may_contact_someone == YES:
                info = (
                    '{info}\n Contacts of someone else:\n'
                    '{contact_name} - {contact_rel}\n'
                    '{contact_cell} (cell), {contact_phone} (phone)\n'
                    '').format(
                        info=info,
                        contact_name=self.contact_name or '(name?)',
                        contact_rel=self.contact_rel or '(relation?)',
                        contact_cell=self.contact_cell or '(----)',
                        contact_phone=self.contact_phone or '(----)'
                )
            if info:
                info = ('{info}'
                        'Physical Address:\n{physical_address}').format(
                            info=info, physical_address=self.physical_address)
        return info

    class Meta(RequiresConsentFieldsModelMixin.Meta):
        consent_model = 'cancer_subject.subjectconsent'
