from ..models import BHHHivTest
from .form_mixins import SubjectModelFormMixin


class BHHHivTestForm (SubjectModelFormMixin):

    class Meta:
        model = BHHHivTest
        fields = '__all__'
