from .subject_off_study_mixin import SubjectOffStudyMixin


class BaseSubjectRegisteredSubjectModel(SubjectOffStudyMixin):

    class Meta:
        abstract = True
