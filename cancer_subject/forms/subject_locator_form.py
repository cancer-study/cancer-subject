from django import forms

from ..models import SubjectLocator
from .form_mixins import SubjectModelFormMixin


class SubjectLocatorForm (SubjectModelFormMixin):

    subject_identifier = forms.CharField(
        label='Subject identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = SubjectLocator
        fields = '__all__'
