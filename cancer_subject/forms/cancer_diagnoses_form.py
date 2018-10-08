from django import forms


from edc_constants.constants import YES, NO

from ..models import CancerDiagnosis
from .form_mixins import SubjectModelFormMixin


# CancerDiagnosis
class CancerDiagnosisForm (SubjectModelFormMixin):

    class Meta:
        model = CancerDiagnosis
        fields = '__all__'
