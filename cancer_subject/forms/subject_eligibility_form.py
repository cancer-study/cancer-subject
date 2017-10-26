from django import forms
from edc_base.modelform_mixins import CommonCleanModelFormMixin


class SubjectModelFormMixin(CommonCleanModelFormMixin, forms.ModelForm):

    pass


class SubjectEligibilityForm(SubjectModelFormMixin):

    class Meta:
        model = SubjectEligibility
        fields = '__all__'
