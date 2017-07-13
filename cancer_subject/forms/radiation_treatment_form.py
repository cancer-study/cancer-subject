from ..models import RadiationTreatment
from .modelform_mixin import SubjectModelFormMixin


class RadiationTreatmentForm (SubjectModelFormMixin):

    class Meta:
        model = RadiationTreatment
        fields = '__all__'
