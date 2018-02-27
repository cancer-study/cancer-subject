from .modelform_mixin import SubjectModelFormMixin
from ..models import HaartMedRecord


class HaartMedRecordForm (SubjectModelFormMixin):

    class Meta:
        model = HaartMedRecord
        fields = '__all__'
