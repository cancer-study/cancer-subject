
from .subject_off_study_mixin import SubjectOffStudyMixin
from .subject_off_study import SubjectOffStudy


class BaseSubjectRegistrationModel(SubjectOffStudyMixin):

    def get_off_study_cls(self):
        return SubjectOffStudy

    class Meta:
        abstract = True
