from ..models import HaartRecord
from .form_mixins import SubjectModelFormMixin


class HaartRecordForm(SubjectModelFormMixin):

    class Meta:
        model = HaartRecord
        fields = '__all__'
