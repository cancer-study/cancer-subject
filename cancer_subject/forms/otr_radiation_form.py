from .form_mixins import SubjectModelFormMixin
from ..models import OTRRadiation


class OTRRadiationForm (SubjectModelFormMixin):

    class Meta:
        model = OTRRadiation
        fields = '__all__'
