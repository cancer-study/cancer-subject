from ..models import LabResultHiv
from .form_mixins import SubjectModelFormMixin


class LabResultHivForm(SubjectModelFormMixin):

    class Meta:
        model = LabResultHiv
        fields = '__all__'
