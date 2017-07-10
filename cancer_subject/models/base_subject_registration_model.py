from edc.subject.registration.models import BaseRegistrationModel

from ..managers import SubjectRegistrationModelManager
from .subject_off_study_mixin import SubjectOffStudyMixin
from .subject_off_study import SubjectOffStudy


class BaseSubjectRegistrationModel(SubjectOffStudyMixin, BaseRegistrationModel):

    objects = SubjectRegistrationModelManager()

    def get_off_study_cls(self):
        return SubjectOffStudy

    class Meta:
        abstract = True
