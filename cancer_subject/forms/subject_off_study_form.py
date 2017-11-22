from edc_offstudy.modelform_mixins import OffStudyFormMixin

from ..models.subject_offstudy import SubjectOffstudy

from .form_mixins import SubjectModelFormMixin


class SubjectOffStudyForm (OffStudyFormMixin, SubjectModelFormMixin):

    class Meta:
        model = SubjectOffstudy
        fields = '__all__'
