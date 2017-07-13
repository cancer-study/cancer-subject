from .subject_off_study_mixin import SubjectOffStudyMixin


class SubjectBaseUuidModel(SubjectOffStudyMixin):

    """ Base model for all subject models """

    class Meta:
        abstract = True
