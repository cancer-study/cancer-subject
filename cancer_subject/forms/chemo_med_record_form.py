from .modelform_mixin import SubjectModelFormMixin
from ..models import ChemoMedRecord


class ChemoMedRecordForm (SubjectModelFormMixin):

    class Meta:
        model = ChemoMedRecord
        fields = '__all__'
