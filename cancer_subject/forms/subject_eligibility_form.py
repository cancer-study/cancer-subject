from django import forms
from edc_base.modelform_mixins import CommonCleanModelFormMixin
from ..models.subject_eligibility import SubjectEligibility


class SubjectModelFormMixin(CommonCleanModelFormMixin, forms.ModelForm):

    pass


class SubjectEligibilityForm(SubjectModelFormMixin):

    class Meta:
        model = SubjectEligibility
        fields = '__all__'
