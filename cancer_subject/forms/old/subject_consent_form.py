import re
from django import forms

from ..models import SubjectConsent
from .form_mixins import SubjectModelFormMixin


class SubjectConsentForm (SubjectModelFormMixin):

    def clean(self):
        cleaned_data = super(SubjectConsentForm, self).clean()
        self.validate_caps("FIRSTNAME", cleaned_data.get('first_name'))
        self.validate_caps("LASTNAME", cleaned_data.get('last_name'))
#         first_name = cleaned_data.get('first_name')
#         last_name = cleaned_data.get('last_name')
#         if first_name.islower():
#             raise forms.ValidationError('PLEASE USE CAPS for FIRSTNAME')
#         if last_name.islower():
#             raise forms.ValidationError('PLEASE USE CAPS for LASTNAME')
        return cleaned_data

    def validate_caps(self, field_name, field_value):
        caps = re.compile('^[A-Z/\s/]{1,50}[A-Z]{1,50}$')
        if caps.match(field_value):
            True
        else:
            raise forms.ValidationError(
                'PLEASE USE ALL CAPS FOR {}'.format(field_name))

    class Meta:
        model = SubjectConsent
