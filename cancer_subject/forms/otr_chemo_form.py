from .form_mixins import SubjectModelFormMixin
from ..models import OTRChemo


class OTRChemoForm (SubjectModelFormMixin):

    class Meta:
        model = OTRChemo
        fields = '__all__'
