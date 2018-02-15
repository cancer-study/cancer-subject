from ..models import BHHCd4
from .form_mixins import SubjectModelFormMixin


class BHHCd4Form (SubjectModelFormMixin):

    class Meta:
        model = BHHCd4
        fields = '__all__'
