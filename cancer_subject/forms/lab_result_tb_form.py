from django import forms

from ..models import LabResultTb
from .form_mixins import SubjectModelFormMixin


class LabResultTbForm(SubjectModelFormMixin):

    class Meta:
        model = LabResultTb
        fields = '__all__'
