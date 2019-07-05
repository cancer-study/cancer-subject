from .form_mixins import SubjectModelFormMixin
from ..models import Referral


class ReferralForm (SubjectModelFormMixin):

    class Meta:
        model = Referral
        fields = '__all__'
