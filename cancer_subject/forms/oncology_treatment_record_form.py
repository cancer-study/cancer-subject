from .modelform_mixin import SubjectModelFormMixin
from ..models import OncologyTreatmentRecord


class OncologyTreatmentRecordForm (SubjectModelFormMixin):

    class Meta:
        model = OncologyTreatmentRecord
        fields = '__all__'
