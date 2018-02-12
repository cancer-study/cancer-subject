from .form_mixins import SubjectModelFormMixin
from ..models import OTRSurgical


class OTRSurgicalForm (SubjectModelFormMixin):

    class Meta:
        model = OTRSurgical
        fields = '__all__'
