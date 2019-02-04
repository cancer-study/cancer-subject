from ..models import LabResult
from .modelform_mixin import SubjectModelFormMixin


class LabResultForm (SubjectModelFormMixin):

    class Meta:
        model = LabResult
        fields = '__all__'
