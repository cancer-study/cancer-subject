from django import forms
from django.contrib.admin.widgets import AdminRadioSelect

from ..choices.subject_off_study import OFF_STUDY_REASON
from ..models import SubjectOffStudy
from .form_mixins import SubjectModelFormMixin


class SubjectOffStudyForm (SubjectModelFormMixin):

    reason = forms.ChoiceField(
        label='Please code the primary reason participant taken off-study',
        choices=[choice for choice in OFF_STUDY_REASON],
        help_text="",
        widget=AdminRadioSelect(renderer=AdminRadioFieldRenderer),)

    class Meta:
        model = SubjectOffStudy
