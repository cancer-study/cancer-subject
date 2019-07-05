from ..models import LabResultCd4
from .form_mixins import SubjectModelFormMixin


class LabResultCd4Form(SubjectModelFormMixin):

    class Meta:
        model = LabResultCd4
        fields = '__all__'
