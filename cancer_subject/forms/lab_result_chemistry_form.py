from ..models import LabResultChemistry
from .form_mixins import SubjectModelFormMixin


class LabResultChemistryForm(SubjectModelFormMixin):

    class Meta:
        model = LabResultChemistry
        fields = '__all__'
