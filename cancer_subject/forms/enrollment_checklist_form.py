from django import forms
# from edc_base.modelform_mixins import CommonCleanModelFormMixin

from ..models import EnrollmentChecklist


class SubjectModelFormMixin(forms.ModelForm):

    pass


class EnrollmentChecklistForm(SubjectModelFormMixin):

    class Meta:
        model = EnrollmentChecklist
        fields = '__all__'
