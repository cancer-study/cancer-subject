from .modelform_mixin import SubjectModelFormMixin
from ..models import OncologyTreatmentCompleted


class OncologyTreatmentCompletedForm (SubjectModelFormMixin):

    class Meta:
        model = OncologyTreatmentCompleted
        fields = '__all__'
