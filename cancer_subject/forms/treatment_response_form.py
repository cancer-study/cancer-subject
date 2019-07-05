from .form_mixins import SubjectModelFormMixin
from ..models import TreatmentResponse


class TreatmentResponseForm (SubjectModelFormMixin):

    class Meta:
        model = TreatmentResponse
        fields = '__all__'
