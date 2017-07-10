from edc.subject.off_study.mixins.off_study_mixin import OffStudyMixin


class SubjectOffStudyMixin(OffStudyMixin):

    def get_off_study_cls(self):
        from .subject_off_study import SubjectOffStudy
        return SubjectOffStudy
