from ..models import LabResultHeightWeight
from .form_mixins import SubjectModelFormMixin


class LabResultHeightWeightForm(SubjectModelFormMixin):

    class Meta:
        model = LabResultHeightWeight
        fields = '__all__'
