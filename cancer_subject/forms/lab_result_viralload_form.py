from ..models import LabResultViralload
from .form_mixins import SubjectModelFormMixin


class LabResultViralloadForm(SubjectModelFormMixin):

    class Meta:
        model = LabResultViralload
        fields = '__all__'
