from edc_offstudy.modelform_mixins import OffstudyModelFormMixin

from ..models.subject_offstudy import SubjectOffstudy

from .form_mixins import SubjectModelFormMixin


class SubjectOffStudyForm (OffstudyModelFormMixin, SubjectModelFormMixin):

    class Meta:
        model = SubjectOffstudy
        fields = '__all__'
