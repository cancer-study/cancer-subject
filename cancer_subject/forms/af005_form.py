from ..models import Af005
from .form_mixins import SubjectModelFormMixin


class Af005Form (SubjectModelFormMixin):

    class Meta:
        model = Af005
        fields = '__all__'
