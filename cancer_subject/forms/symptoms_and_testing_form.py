from django import forms
from edc_constants.constants import YES, NO

from ..models import SymptomsAndTesting
from .form_mixins import SubjectModelFormMixin


class SymptomsAndTestingForm (SubjectModelFormMixin):

    class Meta:
        model = SymptomsAndTesting
        fields = '__all__'
