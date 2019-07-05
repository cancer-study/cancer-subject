from ..models import LabResultHaematology
from .form_mixins import SubjectModelFormMixin


class LabResultHaematologyForm(SubjectModelFormMixin):

    class Meta:
        model = LabResultHaematology
        fields = '__all__'
