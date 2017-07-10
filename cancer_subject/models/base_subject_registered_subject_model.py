from edc.subject.registration.models.base_registered_subject_model import BaseRegisteredSubjectModel
from .subject_off_study_mixin import SubjectOffStudyMixin


class BaseSubjectRegisteredSubjectModel(SubjectOffStudyMixin, BaseRegisteredSubjectModel):

    class Meta:
        abstract = True
