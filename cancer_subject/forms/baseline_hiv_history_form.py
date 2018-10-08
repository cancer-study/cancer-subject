from django import forms
from edc_constants.constants import YES, NO

from ..models import BaselineHIVHistory
from .form_mixins import SubjectModelFormMixin


# BaselineHIVHistory
class BaselineHIVHistoryForm (SubjectModelFormMixin):

    class Meta:
        model = BaselineHIVHistory
        fields = '__all__'
