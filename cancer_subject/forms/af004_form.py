from ..models import Af004
from .form_mixins import SubjectModelFormMixin


class Af004Form(SubjectModelFormMixin):

    class Meta:
        model = Af004
        fields = '__all__'
