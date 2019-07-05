from ..models import Ae010
from .form_mixins import SubjectModelFormMixin


class Ae010Form(SubjectModelFormMixin):

    class Meta:
        model = Ae010
        fields = '__all__'
