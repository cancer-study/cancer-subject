from .modelform_mixin import SubjectModelFormMixin

from ..models import LabResult


# LabResult
class LabResultForm (SubjectModelFormMixin):

    class Meta:
        model = LabResult
        fields = '__all__'
