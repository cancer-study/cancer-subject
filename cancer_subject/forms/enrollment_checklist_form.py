from django import forms

from ..models import EnrollmentChecklist


class SubjectModelFormMixin(forms.ModelForm):

    pass


class EnrollmentChecklistForm(SubjectModelFormMixin):

    subject_identifier = forms.CharField(
        label='Subject identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = EnrollmentChecklist
        fields = '__all__'
