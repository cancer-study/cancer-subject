from django.db import models
from django.core.urlresolvers import reverse

from edc.subject.consent.models import BaseConsent
from edc.subject.consent.mixins import ReviewAndUnderstandingFieldsMixin
from edc.subject.consent.mixins.bw import IdentityFieldsMixin
from edc.subject.registration.models import RegisteredSubject

from .subject_off_study_mixin import SubjectOffStudyMixin


class BaseSubjectConsent(SubjectOffStudyMixin, BaseConsent):

    registered_subject = models.OneToOneField(RegisteredSubject, editable=False, null=True)

    def get_subject_type(self):
        return 'subject'

    def get_subject_identifier(self):
        return self.subject_identifier

    class Meta:
        abstract = True

# add Mixin fields to abstract class
for field in IdentityFieldsMixin._meta.fields:
    if field.name not in [fld.name for fld in BaseSubjectConsent._meta.fields]:
        field.contribute_to_class(BaseSubjectConsent, field.name)

for field in ReviewAndUnderstandingFieldsMixin._meta.fields:
    if field.name not in [fld.name for fld in BaseSubjectConsent._meta.fields]:
        field.contribute_to_class(BaseSubjectConsent, field.name)
