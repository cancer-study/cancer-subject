from django import forms
from edc_constants.constants import YES, NO
from edc_form_validators import FormValidatorMixin
from edc_locator.forms import SubjectLocatorFormValidator as BaseSubjectLocatorFormValidator

from ..models import SubjectLocator


class SubjectLocatorFormValidator(BaseSubjectLocatorFormValidator):

    def validate_indirect_contact(self):
        self.required_if(
            YES, field='may_contact_indirectly',
            field_required='indirect_contact_name')

        self.required_if(
            YES, field='may_contact_indirectly',
            field_required='indirect_contact_relation')

        for field in ['indirect_contact_cell', 'indirect_contact_cell_alt',
                      'indirect_contact_phone']:
            self.not_required_if(
                NO, field='may_contact_indirectly', field_required=field,
                inverse=False)


class SubjectLocatorForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = SubjectLocatorFormValidator

    subject_identifier = forms.CharField(
        label='Subject Identifier',
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = SubjectLocator
        fields = '__all__'
