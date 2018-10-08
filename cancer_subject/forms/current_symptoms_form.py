from django import forms

from edc_constants.constants import YES

from ..models import CurrentSymptoms
from .form_mixins import SubjectModelFormMixin


class CurrentSymptomsForm (SubjectModelFormMixin):

    class Meta:
        model = CurrentSymptoms
        fields = '__all__'
