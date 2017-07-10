from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail

from apps.cancer_subject.models import BaseSubjectConsent


class SubjectConsent(BaseSubjectConsent):

    original_identifier = models.CharField(
        max_length=25,
        null=True,
        blank=True,
        editable=False,
        #validators=[RegexValidator(r'045\-[0-9]{3}\-[0-9]{4}', 'Invalid. Format of original_identifier is 045-999-9999'), ],
        help_text="To be entered ONLY if you are keying old crf forms that have a barcode sticker",
        )

    history = AuditTrail()

    def get_registered_subject(self):
        return self.registered_subject

    def get_user_provided_subject_identifier_attrname(self):
        """override to return the attribute name of the user provided subject_identifier."""
        return 'original_identifier'

    def get_absolute_url(self):
        return reverse('admin:cancer_subject_subjectconsent_change', args=(self.id,))

    class Meta:
        app_label = 'cancer_subject'
        verbose_name = 'Subject Consent'
