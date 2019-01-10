from django import forms

from ..models import SubjectScreening


class SubjectModelFormMixin(forms.ModelForm):

    pass


class SubjectScreeningForm(SubjectModelFormMixin):

    subject_identifier = forms.CharField(
        label='Subject identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = SubjectScreening
        fields = '__all__'
