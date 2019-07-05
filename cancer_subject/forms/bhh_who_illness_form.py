from ..models import BHHWhoIllness
from .form_mixins import SubjectModelFormMixin


class BHHWhoIllnessForm (SubjectModelFormMixin):

    class Meta:
        model = BHHWhoIllness
        fields = '__all__'
